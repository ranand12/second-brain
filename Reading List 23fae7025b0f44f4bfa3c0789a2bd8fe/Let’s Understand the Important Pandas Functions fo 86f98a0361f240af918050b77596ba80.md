# Let’s Understand the Important Pandas Functions for Data Science | by Rahul Kotecha | Dec, 2021 | Python in Plain English

Column: https://python.plainenglish.io/lets-understand-important-pandas-functions-for-data-science-52f42160b8e8
Processed: No
created on: December 31, 2021 7:45 AM
rating: ⭐⭐⭐⭐⭐
topics: money, python, tech-stuff

[](Let%E2%80%99s%20Understand%20the%20Important%20Pandas%20Functions%20fo%2086f98a0361f240af918050b77596ba80/0YLCBRry99cIsBZ2v)

Photo by [Arnold Francisca](https://unsplash.com/@clark_fransa?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Pandas stands for Panel-Data. Pandas is an open-source Python library providing high-performance data manipulation and analysis tools using its powerful data structures. The name Pandas is derived from the word Panel Data — an Econometrics from Multidimensional data. In 2008, developer Wes McKinney started developing pandas when in need of a high-performance, flexible tool for the analysis of data. Prior to Pandas, Python was majorly used for data munging and preparation.

With the understanding of this, we now move on to find out exactly how does Pandas really deal with data and help us get a solution to a number of questions in regards to the data. For the purpose of understanding the important Pandas functions, we will undertake a Case Study dataset and implement Pandas functions.

You will find the following functions being used:

1. `.head()` — Helps show only the first 5 rows of the data and the other rows follow the same format
2. `.tail()` — Shows the last 5 rows of the data set
3. `.info()` — Provides information about the datatype of the column, the number of rows and columns, etc.
4. `.unique()` and `.nunique()` — Unique() helps to print the list of all the unique elements and nunique() gives the number of unique elements present.
5. `.mean()`, `.median()`, `.mode()` — Mean is the average, Median is the middle value and Mode is the element with the maximum occurrence or frequency.
6. `.min()` and `.max()` — Min helps to find the minimum or the lowest value in the data and the max is used to find the maximum or the highest value of the data.
7. `.dtypes` and `.columns` — Dtypes prints the column name and the datatype of the content. The columns function is used to print the list of all the column names in the dataset.
8. `.apply()` — Apply function helps to implement a function to a data set which can either be a user-defined function or an in-built function or an anonymous function.
9. `.value_counts()` — The value_counts function helps by counting the frequency of occurrence of an element in a data set.
10. `.sort_values()` and `.sort_values(ascending=False)` — The sort function can be used to sort data based on ascending or descending order.
11. `.describe()` and `.describe(include=[“object”])` — The describe function helps with statistical information like mean, min value, max value, quartiles etc. In case of an object it counts total count, frequency, etc.
12. `.shape()` — The shape function provides information regarding the total number of rows and columns in a data set.
13. `.astype()` — The astype function helps to change the datatype of a data.
14. `Filtering` — The filtering function is similar to the masking function as seen in numpy and returns only those values that fulfil the condition as True.
15. `.corr()` and `.cov()` — The corr and cov functions are used to find correlation and covariance between two random variables.

**Importing Numpy, Pandas and Warnings**

**Using .head()**

**Using .info()**

**Using .tail()**

**Using .shape()**

**Using .dtypes**

**Using .describe()**

**Using .describe(include=[“object])**

**Finding solution to question using Filtering**

**Using .loc() or Location**

**Using .iloc() or Index Location**

**Filtering**

**Filtering .tail()**

**FInding solution using max()**

**Finding solution using min()**

**Using .mean() and .median()**

**Using .isna() along with .sum()**

**Using .isin()**

**Using .memory_usage()**

**Using .mode() and .max()**

**Using .value_counts()**

**Using .astype()**

**Using .apply() which helps to apply defined or lambda functions to data**

**Using .corr() for Correlation and .cov() for Covariance**

**Using .groupby but Groupby returns an object so using mean to find answer**

**Using .unique() and .nunique()**

**Sort_values for a single column -Ascending order**

**Sort_values for a single column -Descending order**

**Sort_values for the entire data sheet using TotalPay Ascending Order**

**Sort_values for the entire data sheet using TotalPay Descending Order**

**Using .columns and Multi-column selection**

*More content at [plainenglish.io](http://plainenglish.io/). Sign up for our [free weekly newsletter](http://newsletter.plainenglish.io/). Get exclusive access to writing opportunities and advice in our [community Discord](https://discord.gg/GtDtUAvyhW).*