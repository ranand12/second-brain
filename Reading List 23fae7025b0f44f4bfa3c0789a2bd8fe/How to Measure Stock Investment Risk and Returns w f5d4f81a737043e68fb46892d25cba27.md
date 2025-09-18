# How to Measure Stock Investment Risk and Returns with Python | by Bee Guan Teo | Python in Plain English

Column: https://python.plainenglish.io/how-to-measure-stock-investment-risk-and-returns-with-python-5113fa895411
Processed: No
created on: December 31, 2021 7:36 AM
topics: money, python, tech-stuff

![](How%20to%20Measure%20Stock%20Investment%20Risk%20and%20Returns%20w%20f5d4f81a737043e68fb46892d25cba27/15rXejhcKLorK7JiXnQH-tg.jpeg)

Photo by [Scott Graham](https://unsplash.com/@homajob?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/stock-portfolio?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

In the financial market, an [**investment risk**](https://www.investopedia.com/terms/r/risk.asp) refers to a measure of uncertainty of financial returns. Learning the risks can help an investor to minimize unnecessary losses and maximize the profit at the same time.

In this article, I will introduce four [statistical moments](https://en.wikipedia.org/wiki/Moment_(mathematics)) which are commonly used in measuring investment risk:

- **First moment — Mean**
- **Second moment — Variance**
- **Third moment — Skewness**
- **Fourth moment — Kurtosis**

The four statistical moments will be coded in **Python** to measure the investment risk for a selected stock.

**Disclaimer**: The writing of this article is only aimed at demonstrating the investment risk and returns analysis of a stock using Python. It doesn’t serve any purpose of promoting any stock or giving any specific investment advice.

# Prerequisite Python Libraries

1. **yFinance** — [https://pypi.org/project/yfinance/](https://pypi.org/project/yfinance/)
2. **Scipy** — [https://www.scipy.org/](https://www.scipy.org/)
3. **Matplotlib** — [https://matplotlib.org/](https://matplotlib.org/)
4. **Numpy** — [https://numpy.org/](https://numpy.org/)
5. **Pandas** — [https://pandas.pydata.org/](https://pandas.pydata.org/)

# Stock Investment Risk and Returns Analysis

## 1. Acquisition of stock data

We start by using *yFinance* library to obtain stock data from Yahoo Finance. *yFinance* is a very useful open-source library that allows us to acquire up-to-date stock data for any financial analysis.

**Line 1–8:** Import all the required libraries

**Line 11–12:** Set a ticker symbol (e.g. msft) and use *yFinance download* method to download the stock data for that ticker between the range of *start* and *end* date. This will return the stock data as a *Pandas* dataframe.

Image Prepared by the Author

## 2. Visualizing Daily Stock Returns

The stock investment return can be calculated as the daily percentage change of stock price compared with the previous day.

**Line 1:** Use the *pct_change* method to calculate the daily percentage change of the stock adjusted close price and assign the values to a new column, “*Returns*”, in the dataframe.

**Line 2–3:** Use the *plot* method to create a line plot to show the daily percentage change of the adjusted close price.

Image Prepared by the Author

From the line plot, we can see the daily returns are volatile and the values oscillate between positive and negative zones.

We can also create a histogram to visualize the distribution of the returns.

**Line 1–2:** Convert the daily return from decimal to percentage and remove all the null values using the *dropna* method.

**Line 4–6:** Use the *hist* method to plot a histogram.

Image Prepared by the Author

The histogram shows that the daily returns are mostly distributed around -5% to 5%.

## 3. The Mean of Daily and Annual Returns (First Moment)

Here we are going to calculate the mean of the daily returns and its annualized average returns.

**Line 1–2:** Use Numpy *mean* method to calculate the values of the “Returns” column and display the mean.

**Line 4–5:** We presume there are 252 trading days per year and therefore we adopt the following formula to calculate the annual mean returns.

We shall get the following output:

Image Prepared by the Author

On average, the stock gives us an annual mean return of about 0.40%. This project a general idea to us the estimated profit we might earn after one year.

## 4. The variance of returns (Second Moment)

Now let us move on to calculate the variance of returns. The variance is a measurement of the **dispersion of return**. The higher the variance the higher the volatility of the stock price — higher risk.

**Line 1–4:** Use Numpy *std* to calculate the standard deviation of the “Returns” column. Next, presume there are 252 trading days in a year and then apply the following formula to calculate the annual standard deviation of stock returns.

**Line 8–11:** Calculate the variances of daily return and annual return by squaring the daily & annual standard deviation, respectively.

The results are shown below:

Image Prepared by the Author

## 5. Skewness (Third Moment)

[Skewness](https://www.analyticsvidhya.com/blog/2020/07/what-is-skewness-statistics/) is the measurement of asymmetry of a symmetric probability distribution. A normal distribution is the probability distribution with zero skewness.

Image Prepared by the Author

The probability distribution with its tail (elongated segment) on the right side is a positive skew. On another hand, if the tail is on the left side, it is a negative skew.

Image Prepared by the Author

In measuring investment risk, we expect our daily returns are **following the positive skew pattern (positive value)**. This is because more than half of the daily returns are above mean in a positive skew distribution.

Python *Scipy* library offers us a one-liner solution to calculate the skewness of the distribution.

**Line 1:** Use the *dropna* method to remove all the null values from the “Returns” column.

**Line 2–3:** Use the *Scipy skew* function to calculate the skewness of the returns and print it out.

Image Prepared by the Author

The result shows that the skewness is a low negative number and this means it is negatively skewed. From this info, we can learn that the investment of this asset might incur a moderate level of risk.

## 6. Kurtosis (Fourth Moment)

[Kurtosis](https://www.investopedia.com/terms/k/kurtosis.asp) is a measurement of the tail-heaviness of a probability distribution. A distribution with a high kurtosis value will show much larger extreme values on either side of its tails compared with the tails of a normal distribution.

In an investment context, a high kurtosis of the financial return distribution means that the investor might experience occasional extreme returns (positive or negative) which is more extreme than the usual of three standard deviations from the mean of the normal distribution. This phenomenon is known as **kurtosis risk**.

While the concept of kurtosis is seeming too technical, the implementation in Python is very straightforward.

**Line 1–2:** Use the *Scipy kurtosis* function to calculate the **excess kurtosis** from the daily returns. Excess kurtosis is a measurement that compares the kurtosis of distribution against the kurtosis of a normal distribution. If a distribution’s excess kurtosis is more than three, the distribution is leptokurtic.

**Line 3–4:** Calculate the real kurtosis for the daily return distribution by adding three to the *excess_kurtosis*.

We should get the result as follows:

Image Prepared by the Author

The resulting kurtosis value is very high which means an investor of this asset might experience a high kurtosis risk (e.g. unusual drawdown).

# Conclusion

We have already gone through all four statistical moments to assess investment returns and risk. In fact, investment is not only about building a good trading strategy but also establishing a robust risk management that can protect our profit and minimize our loss.

I wish you enjoy reading this article.

## References