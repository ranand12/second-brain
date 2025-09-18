# Pandas Datareader using Python (Tutorial)

Column: https://thecleverprogrammer.com/2021/03/22/pandas-datareader-using-python-tutorial/
Processed: No
created on: December 21, 2021 1:58 PM
topics: money, python, tech-stuff

Pandas Datareader is a Python package that allows us to create a pandas DataFrame object by using various data sources from the internet. It is popularly used for working with realtime stock price datasets. In this article, I will take you through a tutorial on Pandas datareader using Python.

## What is Pandas Datareader in Python?

Pandas Datareader is a Python package that allows us to create a pandas DataFrame by using some popular data sources available on the internet including:

1. ***Yahoo Finance***
2. ***Google Finance***
3. ***Morningstar***
4. ***IEX***
5. ***Robinhood***
6. ***Engima***
7. ***Quandl***
8. ***FRED***
9. ***World Bank***
10. ***OECD and many more.***

All of the data sources mentioned above provide data in a different format, so collecting data from each source follows a different method. In the section below, I will take you through a tutorial on pandas datareader to collect stock price data from Yahoo Finance.

## Working with Pandas Datareader using Python

I hope you now have understood what is pandas_datareader, now let’s see how to use this package to read the stock price data from yahoo finance using Python. If you have never used it before then you can easily install it by using the pip command; pip install pandas_datareader. Now let’s import the necessary Python libraries that we need for this task:

I will set a start date and an end date that can be easily customized in the same format as in the code below:

Now let’s use the datareader method to store the stock price data of [*Tesla*](https://www.tesla.com/) into a DataFrame:

```
                  High         Low        Open       Close      Volume   Adj Close
Date
2019-12-31   84.258003   80.416000   81.000000   83.666000  51428500.0   83.666000
2020-01-02   86.139999   84.342003   84.900002   86.052002  47660500.0   86.052002
2020-01-03   90.800003   87.384003   88.099998   88.601997  88892500.0   88.601997
2020-01-06   90.311996   88.000000   88.094002   90.307999  50665000.0   90.307999
2020-01-07   94.325996   90.671997   92.279999   93.811996  89410500.0   93.811996
...                ...         ...         ...         ...         ...         ...
2020-12-24  666.090027  641.000000  642.989990  661.770020  22865600.0  661.770020
2020-12-28  681.400024  660.799988  674.510010  663.690002  32278600.0  663.690002
2020-12-29  669.900024  655.000000  661.000000  665.989990  22910800.0  665.989990
2020-12-30  696.599976  668.359985  672.000000  694.780029  42846000.0  694.780029
2020-12-31  718.719971  691.119995  699.989990  705.669983  49649900.0  705.669983

[254 rows x 6 columns]
```

The above output looks the same as what we read from any CSV file. Now let’s visualize this data by using the matplotlib library in Python:

![](Pandas%20Datareader%20using%20Python%20(Tutorial)%202094d734775944d79e711ea56d3a6bf6/tesla.png)

## Summary

So this is how easy it is to read and store the stock price data into a pandas DataFrame. In this article, I collected the stock price data of Tesla from Yahoo Finance. I hope you liked this article on a tutorial on pandas_datareader using Python. Feel free to ask your valuable questions in the comments section below.