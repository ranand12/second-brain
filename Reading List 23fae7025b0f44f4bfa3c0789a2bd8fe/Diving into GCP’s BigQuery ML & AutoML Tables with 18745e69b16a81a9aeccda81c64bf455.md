# Diving into GCP’s BigQuery ML & AutoML Tables with Covid19 Big Data | by Thomas Jaensch | Medium

Column: https://medium.com/@tebugging/diving-into-gcps-bigquery-ml-automl-tables-with-covid19-big-data-3208b2a0d702
Processed: Yes
created on: January 26, 2025 8:34 AM

# Diving into GCP’s BigQuery ML & AutoML Tables with Covid19 Big Data

![](https://miro.medium.com/v2/resize:fill:88:88/0*6NG-f134KuWSgawR.jpeg)

[Thomas Jaensch](https://medium.com/@tebugging?source=post_page---byline--3208b2a0d702--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F2b792e9a784b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40tebugging%2Fdiving-into-gcps-bigquery-ml-automl-tables-with-covid19-big-data-3208b2a0d702&user=Thomas+Jaensch&userId=2b792e9a784b&source=post_page-2b792e9a784b--byline--3208b2a0d702---------------------post_header-----------)

16 min read

·

Mar 26, 2022

Art my daughter Nora produced at daycare

![](https://miro.medium.com/v2/resize:fit:535/1*KDl84iVI_Zkj60d_WISEgg.jpeg)

## Everyone and their mother is doing Machine Learning now.

And with tools like Google Cloud Platform’s [BigQuery ML](https://cloud.google.com/bigquery) and [AutoML](https://cloud.google.com/automl) one doesn’t even have to sift through other ML experts’ Python-Numpy-Scikit-TF-Keras-BlahTorch-Pandas notebook mess for inspiration any longer until Python barfs up a lengthy error stack trace because some API or dependency has changed that’s breaking everything else (even though many of us will still be doing that regardless), with BigQuery ML one can just use SQL and SQL only to create ML models on tabular data and make predictions with remarkably little code, and with AutoML there’s literally no code to write at all. Plus it’s kinda fun to see the little green button show up in the BigQuery UI whenever a query has valid syntax.

![](https://miro.medium.com/v2/resize:fit:616/1*2lL1vF9Dw2jjBiwfZojrDA.png)

Having absorbed and tried to process a good chunk of the available books and articles and Youtube vids on BigQuery ML, I decided it’s about time to venture out on my own and predict something other than Boston housing prices, newborn baby weights, NYC Citibike trip durations, or Chicago taxi trip tips and the like, just to get some more practice in using BigQuery ML, and then build a model with AutoML Tables to see the BigQuery ML models crushed!

Luckily inside of BigQuery, there’s a good number of real world datasets readily available for exploration, and while Covid19 is still a thing, I’ve found a dataset authored by the New York Times that is easy enough to understand and use without a ton of digging and preprocessing, and big enough to throw it at something, anything ML tools, techniques, and algorithms. Here’s the [GitHub](https://github.com/nytimes/covid-19-data) repo for the dataset used below, and this is where it can be found inside of the BigQuery console:

![](https://miro.medium.com/v2/resize:fit:700/1*N1tYAjhmu5yypFVrbiO4TA.png)

![](https://miro.medium.com/v2/resize:fit:700/1*xh3xTngruFFBLVTeQDIL2w.png)

![](https://miro.medium.com/v2/resize:fit:700/1*Q8rec_HjoOo79YRJD1ym7w.png)

One piece of crucial advice when approaching Machine Learning I gathered from studying said books, articles and videos has been to start as simple and stupid as possible, and if something actually seems to be working, only then add more complexity and take it from there.

The above table literally screams [Linear Regression](https://blog.insightdatascience.com/always-start-with-a-stupid-model-no-exceptions-3a22314b9aaa) which is pretty much as simple as it can be from what I’ve learned. Just a handful of feature columns to use to predict: deaths!

Data ranges from January 2020 until March 2022 (the time of writing this post), but since January and February 2020 don’t seem to contain a lot of data like the remaining months they will be excluded from the exploration. To create a training data set, March 2020 through December 2021 will be used, excluding any `Null` values.

Inside the BigQuery UI a dataset needs to be created, like this:

![](https://miro.medium.com/v2/resize:fit:700/1*g8hBtdcine3Gx78dzTzZTQ.png)

The Project ID will be derived from whatever GCP project you’re in at the moment and if you don’t have one yet, you will need to create it and also set up billing. It’s definitely going to be different from mine so if you’re planning on running any of the following queries, this piece has to constantly be updated on your end (plus a few others). Dataset ID can be whatever but in order to follow along with less trouble changing things around I suggest to use what I’m using there. It is important to set the `Data location`to the same thing like above or BigQuery will throw a permissions error when you try to query the public datasets from your own project. No `Advanced options` needed before hitting `CREATE DATASET` .

In BigQuery UI on the lefthand side you should now see your dataset underneath your Project:

![](https://miro.medium.com/v2/resize:fit:700/1*ax_RiUb5QcYoZ2aQ09ehvA.png)

In the BigQuery UI, hit `COMPOSE NEW QUERY` and run the following query to create the training table later to be used to create models with BigQuery ML:

```
CREATE OR REPLACE TABLE `covid19_nyt.training_table` ASSELECTcounty,state_name,confirmed_cases,deathsFROM`bigquery-public-data.covid19_nyt.us_counties`WHEREdate >= '2020-03-01' and date <= '2021-12-31'AND county is not NULLAND state_name is not NULLAND confirmed_cases is not NULLAND deaths is not NULL;
```

On the lefthand side of the UI you will now see the newly created table underneath the `covid19_nyt` dataset:

![](https://miro.medium.com/v2/resize:fit:700/1*FQRRUNfiJy64mnJ_BEJCRQ.png)

We’re leaving the months January, February, and March 2022 for now to have something left to create evaluation and test sets, but more on that later.

The first model we’re going to create with BigQuery ML is going to be a simple Linear Regression model with just the default BigQuery settings without any specific hyperparameter tuning, just to have a baseline for improvements down the line. This model is going to predict the number of deaths from only three dataset parameters, county , state_name , and confirmed_cases :

```
CREATE OR REPLACE MODEL`covid19_nyt.deaths_by_county_linear_regression`OPTIONS(model_type='linear_reg') ASSELECTcounty,state_name,confirmed_cases,deaths as labelFROM`covid19_nyt.training_table`;
```

For me this takes about a minute and the result is a saved model inside the BigQuery `covid19_nyt`dataset:

![](https://miro.medium.com/v2/resize:fit:700/1*aoHrb9rxb5D5WDzYjeTGtA.png)

The evaluation metrics are as follows:

![](https://miro.medium.com/v2/resize:fit:700/1*ANYgkQBJlhR5gQRUOZNVNQ.png)

Let’s see if those will improve by simply changing the model type from Linear Regression to Boosted Trees with XGBoost. There are many options for setting hyperparameters which I am not going to worry about for now (see the documentation here: [https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree)):

```
CREATE OR REPLACE MODEL`covid19_nyt.deaths_by_county_boosted_tree_regression`OPTIONS(model_type='BOOSTED_TREE_REGRESSOR') ASSELECTcounty,state_name,confirmed_cases,deaths as labelFROM`covid19_nyt.training_table`;
```

First thing to notice, it takes about 6 minutes to train this model which is significantly longer than the one for Linear Regression. And judging from the evaluation metrics Mean Absolute Error and Mean Squared Error the model actually looks worse than the previous one:

![](https://miro.medium.com/v2/resize:fit:700/1*J6aDuzk9ru6iw84Y__YQPw.png)

Try a Deep Neural Network Regressor and see what happens:

```
CREATE OR REPLACE MODEL`covid19_nyt.deaths_by_county_dnn_regression`OPTIONS(model_type='DNN_REGRESSOR') ASSELECTcounty,state_name,confirmed_cases,deaths as labelFROM`covid19_nyt.training_table`;
```

That takes about 12 minutes and the metrics look even worse:

![](https://miro.medium.com/v2/resize:fit:700/1*19gpJUA1uTltEePpEJ0xIw.png)

My guess is that for XGBoost and DNN algorithm the training data set with only three features is not complex enough to get a good model so Linear Regression for this simplistic dataset seems to be the best choice.

How to get a better model? More data and/or more features!

As it happens, the `covid19_nyt` BigQuery public dataset contains another table `mask_use_by_county:`

![](https://miro.medium.com/v2/resize:fit:700/1*zyUbICsD93irXZScP_SR0A.png)

Both the `us_counties` table and the `mask_use_by_county` table have one column in common, `county_fips_code` . Maybe those two tables could be joined on that column to increase the number of features and get a better model?

```
CREATE OR REPLACE TABLE`covid19_nyt.training_table` AS (WITHbase_table AS (SELECTuc.date,uc.county,uc.state_name,uc.confirmed_cases,uc.deaths,mu.always,mu.never,mu.rarely,mu.sometimes,mu.frequentlyFROM`bigquery-public-data.covid19_nyt.us_counties` AS ucJOIN`bigquery-public-data.covid19_nyt.mask_use_by_county` AS muONuc.county_fips_code = mu.county_fips_code )SELECTdate,county,state_name,confirmed_cases,deaths,always AS mask_always,never AS mask_never,rarely AS mask_rarely,sometimes AS mask_sometimes,frequently AS mask_frequently,EXTRACT (YEAR FROM date) year,EXTRACT (MONTH FROM date) monthFROMbase_tableWHEREdate > '2020-02-29'AND date < '2022-01-01'AND county IS NOT NULLAND county != 'Unknown'AND state_name IS NOT NULLAND confirmed_cases IS NOT NULLAND deaths IS NOT NULLGROUP BYdate,county,state_name,confirmed_cases,deaths,always,never,rarely,sometimes,frequently,year,monthORDER BYyear, month ASC);
```

And then create a new Linear Regression model with the updated training table:

```
CREATE OR REPLACE MODEL`covid19_nyt.deaths_by_county_linear_regression_joined_tables`OPTIONS(model_type='linear_reg') ASSELECTcounty,confirmed_cases,state_name,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,deaths as labelFROM`covid19_nyt.training_table`;
```

Et voilà, Mean Absolute Error and Mean Squared Error have slightly improved:

![](https://miro.medium.com/v2/resize:fit:700/1*03APAtFENWR5lOYwgT0KwQ.png)

Now try XGBoost with the more complex training table:

```
CREATE OR REPLACE MODEL`covid19_nyt.deaths_by_county_boosted_tree_regression_joined_tables`OPTIONS(model_type='BOOSTED_TREE_REGRESSOR') ASSELECTcounty,confirmed_cases,state_name,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,deaths as labelFROM`covid19_nyt.training_table`;
```

Much better than the first XGBoost model:

![](https://miro.medium.com/v2/resize:fit:700/1*_EuxVGELaih6bcAqHjXgcw.png)

And DNN Regressor:

```
CREATE OR REPLACE MODEL`covid19_nyt.deaths_by_county_dnn_regression_joined_tables`OPTIONS(model_type='DNN_REGRESSOR') ASSELECTcounty,confirmed_cases,state_name,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,deaths as labelFROM`covid19_nyt.training_table`;
```

Also much improved compared to the previous DNN model with simpler training data:

![](https://miro.medium.com/v2/resize:fit:700/1*aM6_KTHZlTKWDKPxpRIWFw.png)

Overall, the 2nd XGBoost model seems to have the best evaluation metrics and model creation time is in between Linear Regression and DNN model so let’s try to improve that model with some hyperparameter tuning:

```
CREATE OR REPLACE MODEL`covid19_nyt.deaths_by_county_boosted_tree_regression_3`OPTIONS(model_type='BOOSTED_TREE_REGRESSOR', BOOSTER_TYPE = 'DART', NUM_PARALLEL_TREE = 3, DART_NORMALIZE_TYPE = 'TREE', TREE_METHOD = 'APPROX', MAX_TREE_DEPTH = 9, EARLY_STOP = TRUE, ENABLE_GLOBAL_EXPLAIN = TRUE) ASSELECTcounty,confirmed_cases,state_name,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,deaths as labelFROM`covid19_nyt.training_table`;
```

And surprisingly, the evaluation metrics have improved further:

![](https://miro.medium.com/v2/resize:fit:700/1*b_Pwhk8snQgcXaQe1DO8jQ.png)

Surprising because the ML expert writing this rather randomly chose a bunch of hyperparameters offered here [https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree)… and it worked!

Since `ENABLE_GLOBAL_EXPLAIN` was turned on, this tab is now available as well that shows the feature importance of the model:

![](https://miro.medium.com/v2/resize:fit:700/1*zJ2JltiaXo8XTxI44HpNBw.png)

Wear your masks, kids!

Time to evaluate the last best model and create an evaluation table with January and February 2022 data that the model hasn’t seen yet:

```
CREATE OR REPLACE TABLE`covid19_nyt.evaluation_table` AS (WITHbase_table AS (SELECTuc.date,uc.county,uc.state_name,uc.confirmed_cases,uc.deaths,mu.always,mu.never,mu.rarely,mu.sometimes,mu.frequentlyFROM`bigquery-public-data.covid19_nyt.us_counties` AS ucJOIN`bigquery-public-data.covid19_nyt.mask_use_by_county` AS muONuc.county_fips_code = mu.county_fips_code )SELECTdate,county,state_name,confirmed_cases,deaths,always AS mask_always,never AS mask_never,rarely AS mask_rarely,sometimes AS mask_sometimes,frequently AS mask_frequently,EXTRACT (YEAR FROM date) year,EXTRACT (MONTH FROM date) monthFROMbase_tableWHEREdate >= '2022-01-01'AND date < '2022-02-28'AND county IS NOT NULLAND county != 'Unknown'AND state_name IS NOT NULLAND confirmed_cases IS NOT NULLAND deaths IS NOT NULLGROUP BYdate,county,state_name,confirmed_cases,deaths,always,never,rarely,sometimes,frequently,year,monthORDER BYyear, month ASC);
```

Then evaluate:

```
SELECT*FROMML.EVALUATE(MODEL`bigquery-ml-344115.covid19_nyt.deaths_by_county_boosted_tree_regression_3`,(SELECTcounty,state_name,confirmed_cases,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,deaths as labelFROM`bigquery-ml-344115.covid19_nyt.evaluation_table`));
```

Results are much worse than on the training data and it looks like that last model is overfitting:

![](https://miro.medium.com/v2/resize:fit:700/1*Dg6CGRt6P1S42-TPQYEFgw.png)

Evaluate the previous `deaths_by_county_boosted_tree_regression_joined_tables` model on the evaluation data and see if that’s any better:

```
SELECT*FROMML.EVALUATE(MODEL`bigquery-ml-344115.covid19_nyt.deaths_by_county_boosted_tree_regression_joined_tables`,(SELECTcounty,state_name,confirmed_cases,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,deaths as labelFROM`bigquery-ml-344115.covid19_nyt.evaluation_table`));
```

Sadly, not better:

![](https://miro.medium.com/v2/resize:fit:700/1*4JKMXvTWnPQIFnJNfIoozQ.png)

How about the `deaths_by_county_linear_regression_joined_tables` model?

```
SELECT*FROMML.EVALUATE(MODEL`bigquery-ml-344115.covid19_nyt.deaths_by_county_linear_regression_joined_tables`,(SELECTcounty,state_name,confirmed_cases,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,deaths as labelFROM`bigquery-ml-344115.covid19_nyt.evaluation_table`));
```

Also worse than the best XGBoost model:

![](https://miro.medium.com/v2/resize:fit:700/1*tzWO6QnADToCvoM_pix3ug.png)

Best XGBoost model seems to be overfitting the training data, how about adding some L2 regularization? L1 doesn’t seem to make sense here since there aren’t that many features to begin with.

```
CREATE OR REPLACE MODEL`covid19_nyt.deaths_by_county_boosted_tree_regression_l2`OPTIONS(model_type='BOOSTED_TREE_REGRESSOR', BOOSTER_TYPE = 'DART', NUM_PARALLEL_TREE = 3, DART_NORMALIZE_TYPE = 'TREE', TREE_METHOD = 'APPROX', MAX_TREE_DEPTH = 9, EARLY_STOP = TRUE, ENABLE_GLOBAL_EXPLAIN = TRUE, L2_REG = 0.1) ASSELECTcounty,confirmed_cases,state_name,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,deaths as labelFROM`covid19_nyt.training_table`;
```

Evaluate again:

![](https://miro.medium.com/v2/resize:fit:700/1*6gRV9BRSWv-1MgJDy3dwkg.png)

A bit better but still overfitting. Reduce `MAX_TREE_DEPTH` from 9 to 7:

```
CREATE OR REPLACE MODEL`covid19_nyt.deaths_by_county_boosted_tree_regression_l2`OPTIONS(model_type='BOOSTED_TREE_REGRESSOR', BOOSTER_TYPE = 'DART', NUM_PARALLEL_TREE = 3, DART_NORMALIZE_TYPE = 'TREE', TREE_METHOD = 'APPROX', MAX_TREE_DEPTH = 7, EARLY_STOP = TRUE, ENABLE_GLOBAL_EXPLAIN = TRUE, L2_REG = 0.1) ASSELECTcounty,confirmed_cases,state_name,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,deaths as labelFROM`covid19_nyt.training_table`;
```

Evaluate again (same query as above since model name is the same), results:

![](https://miro.medium.com/v2/resize:fit:700/1*tpjgjkRpocmDdjXMLKgMLg.png)

Sadly, it’s worse again. Funny enough, the 2nd DNN Regression model works better on the evaluation data than everything else before:

```
SELECT*FROMML.EVALUATE(MODEL`bigquery-ml-344115.covid19_nyt.deaths_by_county_dnn_regression_joined_tables`,(SELECTcounty,state_name,confirmed_cases,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,deaths as labelFROM`bigquery-ml-344115.covid19_nyt.evaluation_table`));
```

![](https://miro.medium.com/v2/resize:fit:700/1*yz1AHqfu4OT4PL0dglYdAg.png)

I could go on and on here experimenting with different model hyperparameters, feature engineering like feature crosses, algorithms (like Wide-and-Deep Networks which are also available in BigQuery ML but most likely take even longer than DNNs to train, see the documentation here [https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-wnd-models](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-wnd-models)), or I could just throw the 2nd training table at AutoML Tables which can be invoked from the BigQuery UI ([https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-automl](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-automl)) or, even easier, from here: [https://cloud.google.com/automl-tables/docs](https://cloud.google.com/automl-tables/docs)

Go to this link [https://cloud.google.com/automl-tables/docs/quickstart](https://cloud.google.com/automl-tables/docs/quickstart) and follow the below steps:

![](https://miro.medium.com/v2/resize:fit:700/1*GbckDCkM4nE_hZEekmD0FQ.png)

The last blue button above will take you to this page:

![](https://miro.medium.com/v2/resize:fit:700/1*JVBYTiRo1J9rZHg7J0bD1Q.png)

Click `NEW DATASET` and enter this:

![](https://miro.medium.com/v2/resize:fit:700/1*crx0V7M2By2jquz2Ak_Y1A.png)

Click `CREATE DATASET` and on the next screen, do this (for `BigQuery Project ID` you have to enter your own project ID, everything else should be the same if you’ve followed along):

![](https://miro.medium.com/v2/resize:fit:700/1*P6Xn4MPTNRd68RmTZIdPAA.png)

After that you will see this screen for quite some time:

![](https://miro.medium.com/v2/resize:fit:700/1*-IRWJSuw4XcRbzfzxQmBVQ.png)

You will receive an email like below when the dataset has finished importing:

![](https://miro.medium.com/v2/resize:fit:700/1*0U4hobzSmNkIByoZvGg9lQ.png)

On the AutoML Tables Datasets page, click on the imported dataset:

![](https://miro.medium.com/v2/resize:fit:700/1*nC3Yrjz_eIZSoo_56Q18sw.png)

On the next page, click on “Select a column” under `Target column` and choose `deaths`:

![](https://miro.medium.com/v2/resize:fit:700/1*vS-WnoG5SG_L_sDK6ddZxA.png)

Then click `TRAIN MODEL` which is going to appear on the righthand side.

On the next dialogue, enter a value between 1 and 72 hours to train the AutoML model:

![](https://miro.medium.com/v2/resize:fit:700/1*wC-OllwAkXB1gcEQMrzkLA.png)

And then wait for however long you chose to train… for this example it was 8 hours.

![](https://miro.medium.com/v2/resize:fit:700/1*DBYhTnyzbZJ_sfJnnOg21Q.png)

Go take another [From-Zero-To-Hero ML course on Udemy](https://www.udemy.com/course/applied-machine-learning-hands-on-course/), or [smoke a brisket](https://www.youtube.com/watch?v=R0Lya2nQ3XQ), or go on a 3-day bender for the full 72 hour training time, until you finally receive an email like below if everything checked out:

![](https://miro.medium.com/v2/resize:fit:700/1*R1mq-s7oJUhYhNhD-W_nBQ.png)

The metrics of the AutoML model look tons better out of the box than anything else before:

![](https://miro.medium.com/v2/resize:fit:700/1*oKwqe1rwEUJglEXlkW7bdg.png)

Feature importance is somewhat different from the overfitting XGBoost model:

![](https://miro.medium.com/v2/resize:fit:700/1*8W3Iwrs72QwY0xexrP_BIA.png)

Export the newly minted model to Cloud Storage. You will need to create a Cloud Storage bucket for this that adheres to certain conditions described in the documentation ([https://cloud.google.com/automl-tables/docs/locations#buckets](https://cloud.google.com/automl-tables/docs/locations#buckets)):

![](https://miro.medium.com/v2/resize:fit:700/1*f2y3FM7rD6-mHbFwc7cIYg.png)

Import the model from Cloud Storage into BigQuery, for me that query looks like this (also see documentation [https://cloud.google.com/bigquery-ml/docs/making-predictions-with-imported-tensorflow-models#console](https://cloud.google.com/bigquery-ml/docs/making-predictions-with-imported-tensorflow-models#console)):

```
CREATE OR REPLACE MODEL covid19_nyt.imported_tf_modelOPTIONS (MODEL_TYPE='TENSORFLOW',MODEL_PATH='gs://covid19_nyt/tf_model/model-export/tbl/tf_saved_model-covid19_nyt_20220324081953-2022-03-25T13:50:20.172589Z/*')
```

![](https://miro.medium.com/v2/resize:fit:700/1*FFq3XvDFErPkyQxIcbbu1A.png)

I then wanted to evaluate the imported AutoML model (see above) like the previous models created with BigQuery ML, but apparently that is not possible as of March 2022: [https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-tensorflow#limitations](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-tensorflow#limitations)

So how to evaluate the AutoML model and the BigQuery ML models on the same evaluation data? Well, apparently that is not a simple task. The exported AutoML TF model cannot be evaluated in BigQuery ML, and there’s no way (or I don’t know it yet) to import BigQuery ML models into AutoML somehow.

Here’s what I came up with: on the `EVALUATE` tab of the AutoML model page is a link `VIEW YOUR EVALUATION RESULTS IN BIGQUERY:`

![](https://miro.medium.com/v2/resize:fit:700/1*rlO1HzNomZWb9mZSjdA6KQ.png)

Clicking that will export the data into BigQuery that AutoML used for evaluation when creating the model:

![](https://miro.medium.com/v2/resize:fit:700/1*ZWGUyhFPUlsDxiWMRiDDFg.png)

So couldn’t that data be used by BigQuery ML models to run the `ML.EVALUATE` function against? Well, that doesn’t work because AutoML apparently changes some of the data types which breaks that functionality. However, that AutoML dataset can be reverse-engineered to match the original format, like this (note you will have to replace the autogenerated stuff with your own values for this to work):

```
CREATE OR REPLACE TABLE`export_evaluated_examples_covid19_nyt_20220324081953_2022_03_25T05_38_44_970Z.evaluated_examples_bq` AS (SELECTcast(date as timestamp) as date,county,state_name,cast(confirmed_cases as int) as confirmed_cases,cast(deaths as int) as deaths,mask_always,mask_frequently,mask_never,mask_rarely,mask_sometimes,cast(year as int) as year,cast(month as int) as monthFROM `bigquery-ml-344115.export_evaluated_examples_covid19_nyt_20220324081953_2022_03_25T05_38_44_970Z.evaluated_examples`);
```

This new table that contains essentially the same data AutoML used to evaluate its model can be used by BigQuery’s `ML.EVALUATE` to evaluate the previously created BigQuery models.

Here are the metrics for the 2nd BigQuery ML DNN Regressor model that seemed to work best on the original 2nd version evaluation data:

![](https://miro.medium.com/v2/resize:fit:700/1*NPusXpXFCzk5tNH8ZOmQXw.png)

Which is way worse than the metrics (like MAE) for the AutoML model on the same evaluation data (199,789 records):

![](https://miro.medium.com/v2/resize:fit:700/1*EbNqC9-aitPeed7WkpvUcg.png)

I tested all the previously created BigQuery ML models but none of them came anywhere near to what the AutoML model achieves so it’s probably safe to say that the latter is the best model out of all the ones created so far.

Now, finally, predictions!

First we are going to create a test set with the data from March 2022 of `covid19_nyt` which has not been used yet by either AutoML model or any of the BigQuery ML models:

```
CREATE OR REPLACE TABLE`covid19_nyt.test_table` AS (WITHbase_table AS (SELECTuc.date,uc.county,uc.state_name,uc.confirmed_cases,uc.deaths,mu.always,mu.never,mu.rarely,mu.sometimes,mu.frequentlyFROM`bigquery-public-data.covid19_nyt.us_counties` AS ucJOIN`bigquery-public-data.covid19_nyt.mask_use_by_county` AS muONuc.county_fips_code = mu.county_fips_code )SELECTdate,county,state_name,confirmed_cases,deaths,always AS mask_always,never AS mask_never,rarely AS mask_rarely,sometimes AS mask_sometimes,frequently AS mask_frequently,EXTRACT (YEAR FROM date) year,EXTRACT (MONTH FROM date) monthFROMbase_tableWHEREdate >= '2022-03-01'AND date <= '2022-03-31'AND county IS NOT NULLAND county != 'Unknown'AND state_name IS NOT NULLAND confirmed_cases IS NOT NULLAND deaths IS NOT NULLGROUP BYdate,county,state_name,confirmed_cases,deaths,always,never,rarely,sometimes,frequently,year,monthORDER BYyear, month ASC);
```

Next, query this test table with the AutoML model through the AutoML UI for batch prediction:

![](https://miro.medium.com/v2/resize:fit:700/1*p2cEPC2mu7B4rU3ZR8hbig.png)

The predictions once it’s done predicting will end up in the BigQuery UI like this:

![](https://miro.medium.com/v2/resize:fit:700/1*LOvwVb-IhPaulJkxB9Ivkw.png)

These predictions can then be joined with the predictions on the test table from any of the BigQuery ML models to generate a direct comparison of actual deaths, AutoML model predicted deaths, and BigQuery ML model predicted deaths, like this:

```
WITHautoml AS (SELECTCAST(date AS date) AS date,county,state_name,CAST(confirmed_cases AS int) AS confirmed_cases,CAST(deaths AS int) AS deaths,(SELECTtables.valueFROMUNNEST(predicted_deaths)) AS predicted_deaths_automl,FROM`bigquery-ml-344115.prediction_covid19_nyt_20220324081953_2022_03_25T10_20_13_527Z.predictions`),bigquery AS (SELECTdate,county,state_name,confirmed_cases,deaths,predicted_label AS predicted_deaths_bq_dnnFROMML.PREDICT(MODEL`covid19_nyt.deaths_by_county_dnn_regression_joined_tables`,(SELECT*FROM`covid19_nyt.test_table`)))SELECTautoml.date,automl.county,automl.state_name,automl.confirmed_cases,automl.deaths,automl.predicted_deaths_automl,bigquery.predicted_deaths_bq_dnnFROMautomlJOINbigqueryONautoml.date = bigquery.dateAND automl.county = bigquery.countyAND automl.state_name = bigquery.state_nameAND automl.confirmed_cases = bigquery.confirmed_casesAND automl.deaths = bigquery.deaths;
```

Which is going to look something like this:

![](https://miro.medium.com/v2/resize:fit:700/1*dIcGnbDLAZdshHSykpGNgw.png)

When I was doing that, there were 75192 records in the test dataset. To be able to see the count of rows where the number for predicted deaths of the AutoML model is closer to the actual test data deaths than predicted by the BigQuery ML model, run this query:

```
WITHautoml AS (SELECTCAST(date AS date) AS date,county,state_name,CAST(confirmed_cases AS int) AS confirmed_cases,CAST(deaths AS int) AS deaths,(SELECTtables.valueFROMUNNEST(predicted_deaths)) AS predicted_deaths_automl,FROM`bigquery-ml-344115.prediction_covid19_nyt_20220324081953_2022_03_25T10_20_13_527Z.predictions` ),
bigquery AS (SELECTdate,county,state_name,confirmed_cases,deaths,predicted_label AS predicted_deaths_bq_dnnFROMML.PREDICT(MODEL`covid19_nyt.deaths_by_county_dnn_regression_joined_tables`,(SELECT*FROM`covid19_nyt.test_table`)) ),
joined_table AS (SELECTautoml.date,automl.county,automl.state_name,automl.confirmed_cases,automl.deaths,automl.predicted_deaths_automl,bigquery.predicted_deaths_bq_dnnFROMautomlJOINbigqueryONautoml.date = bigquery.dateAND automl.county = bigquery.countyAND automl.state_name = bigquery.state_nameAND automl.confirmed_cases = bigquery.confirmed_casesAND automl.deaths = bigquery.deaths )SELECTCOUNT(*) AS automl_better_modelFROMjoined_tableWHEREABS(deaths - predicted_deaths_automl) < ABS(deaths - predicted_deaths_bq_dnn);
```

Results:

![](https://miro.medium.com/v2/resize:fit:700/1*Z6_ZxoVEiHqv62YlsOUlJA.png)

So in about 73.5% of the test cases (55237 out of 75192) the AutoML model makes a more accurate prediction of the Covid19 death counts than the 2nd BigQuery ML DNN Regressor model.

I could now take this AutoML model and try to deploy it in various ways which I’m sure would be really cool, but Google Cloud Platform & APIs already sent me a $100 payment received receipt since I started playing around with querying BigQuery & AutoML and generating models for this write up so I’m not going to do that for just a toy project.

![](https://miro.medium.com/v2/resize:fit:700/1*E84PATd4apSr6u5NeEgqEw.png)

# Bottom Line

BigQuery ML is great and even fun to use on tabular data for building Machine Learning models without a lot of fuss or overhead like one usually encounters when using notebooks and whatever ML libraries float your boat (that said, you could also use those libraries in conjunction WITH notebooks AND BigQuery ML…). Once you think you’ve massaged your tabular data enough for a good baseline to make ML predictions, it’s relatively quick and easy to create different kinds of models. The massaged data could then also be used to get an even better model using AutoML Tables, however, the training times are a lot longer and more costly.

**Note:** If you, dear expert ML reader, find anything in this post to be complete and utter ML BS, wrong, misleading, whatever, or have actual ideas about what I described above could be significantly improved, I’d be happy to learn more about it in the comments!