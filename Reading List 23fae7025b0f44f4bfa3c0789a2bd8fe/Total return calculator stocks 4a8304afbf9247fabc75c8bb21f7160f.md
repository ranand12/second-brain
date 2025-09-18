# Total return calculator stocks

Column: https://dqydj.com/etf-return-calculator/
Processed: No
created on: March 4, 2022 11:33 AM
topics: money

On this page is an *ETF return calculator* which automatically computes total return including reinvested dividends. Enter a starting amount and time-frame to estimate the growth of an investment in an Exchange Traded Fund or use it as an index fund calculator. Additionally, simulate periodic investments into a fund by year, month, week, or day.

There are ***over 2,200 exchange traded funds*** in our database, accurate to within the last 7 trading days.

## ETF Total Return Calculator with Dividend Reinvestment and Periodic Investments

To begin, you need to enter **at least** an ETF's ticker. As you type, it will auto-complete active exchange traded fund tickers.

![](Total%20return%20calculator%20stocks%204a8304afbf9247fabc75c8bb21f7160f/etf-return-calculator-inputs.png)

Basic options for ETF investment simulation modeling.

- **Starting Amount ($):** In dollars, an initial investment amount
- **Starting Date:** Enter when an investment was first made °
- **Ending Date:** Enter when an investment was sold °

° *Depending on the ETF data (see more below), we might adjust the starting date and ending date. Check again after your calculation.*

![](Total%20return%20calculator%20stocks%204a8304afbf9247fabc75c8bb21f7160f/advanced-investment-options.png)

Advanced options concentrating on dividend events and periodic investments

Click 'Toggle Advanced' to open the advanced ETF dividend and investment panel.

- **Show Events:** Check the box and we'll list all our dividend information for the ETF in your timeframe. We'll also include (optionally) periodic investment information.
- **Periodic Investments:** Select the box if you'd like to model periodic investments into an exchange traded fund.
- **"Monthly"**: If you are simulating periodic investments, select the timeframe for the ETF investments.
- **Regular Amount:** The amount invested every period in the simulation.

![](Total%20return%20calculator%20stocks%204a8304afbf9247fabc75c8bb21f7160f/etf-portfolio-model-with-dividends.png)

Results of the total return calculator for DIA

- **Final Value ($):** The value of the ETF investment on the 'Ending Date'. Again, note we may change that date depending on the database refresh limit.
- **Annual Return:** Our estimate of the annualized percentage return by the investment, including any periodic investments. The final value will show the actual ending balance if you want to compute a total return instead. ([See our compound annual growth calculator](https://dqydj.com/cagr-calculator/))
- **Graph:** The value of the ETF investment over time. If you're on desktop, hover over a point to see the investment value snapshot on any day in your scenario.

The tool is backed by a database with OHLC prices on exchange traded funds, and a separate entry for dividends. For your choice of dates, we invest at the open price – for the initial lump sum and any dividends – then calculate the portfolio value at daily close.

If you choose to model periodic investments, they are also added at daily open prices. To make the logic simple, we invest(the next legal market day) 1, 7, 30, or 365 days after the previous investment respective to your time frame choice. If dividends and periodic investments would have occurred on the same day, those calculations are independent.

Using the tool and periodic investments, you can also model dollar cost averaging. Dollar cost averaging is our [preferred normal style of investing](https://dqydj.com/dollar-cost-averaging/), where you invest on a regular basis.

For periodic windfalls you receive, we prefer [investing the lump sum all at once](https://dqydj.com/dollar-cost-averaging-vs-lump-sum/).

## Source and Methodology of the Exchange Traded Fund Total Return Calculator

The ETF return calculator is a derivative of the [stock return calculator](https://dqydj.com/stock-return-calculator/). Much of the features are the same, but (especially for smaller funds) the dividend data might be off.

The tool uses the [IEX Cloud API](https://iexcloud.io/docs/api/) for price and dividend data. IEX isn't free, so we have some very modest limits in place:

- ETF data may be **up to 7 trading days old**. Note: weekend refreshes and market holidays might mean this is over 7 'actual' days'.
    - Always check the tool ending date after a scenario to see data recency of the ETF.
- **Splits are a manual process**
    - I need to manually apply split factors. I might automate these eventually, but be patient for now.
- Here are the **rate limits** in place:
    - Maximum **50** calculations per day
    - Maximum **10** calculations per minute

***The exchange traded fund total return calculated contains idealized return data. It is based on closing and opening prices and would not match a real investor's gains exactly.***

The tool is for informational purposes only. We cannot warrant any results. ETF outputs are good for initial research, but please verify any information the tool outputs independently.

Note that there are other factors the tool is ignoring:

- Taxes
- Your portfolio management fees
- Dividend timing
- Slippage
- Other things

It is very possible that the price or dividend datasets are wrong too (please report it if you find a bug).

### Using the tool as an Index Fund return calculator

Many ETFs track published indexes, so the tool is very useful as a quick comparison on index funds. (Yes, we know – many more are in mutual fund form, we're working on it.)

For the gold standard of index fund returns – perhaps with less resolution – see the prospectus of the fund. This calculator will give you a reasonable approximation of index fund returns, but your ETF provider probably calculated them exactly.

### Bug Reports, Feature Requests, and Requests to Help with the ETF Total Return Calculator

[Let us know](https://dqydj.com/about-us/) if you find a bug. **Include the fund with the issue so I can debug it.**

Feel free to send enhancement requests, just know that the bar is very high. Outside of ads, I'm not paid to build or maintain this tool. For significant requests, please [**make a contracting inquiry](https://dqydj.com/about-us/#contact_us).**

Again, this information is for **informational and research purposes only**. We **cannot and will not be able to help** in a legal capacity. **We can only help you with research inquiries.** For legal inquiries, this data might be a useful starting point, but you probably need a professional known as a "forensic accountant".

## ETFs, Dividends, and Total Returns

We've maintained some version of a stock return calculator for some time now. After a mutual fund return calculator, an ETF return tool has been one of our most popular requests.

When we set out to redo the stock return calculator, ETFs were also in the back of our mind. *We're happy to finally bring it home!*

As we like to stress on this site, dividend adjusted returns are the most important returns. Unless you are shoveling your dividend checks into your fireplace (or shredder), it's real money which you can use to reinvest. Those additional shares also lead to real money. Dividends make up a huge amount of return when you trace them back over a long enough timeframe.

But, really, our aims are altruistic with this tool. For the last decade we've stressed that you need to produce *fair, dividend reinvested return comparisons* when discussing investments.

This tool, in many ways, is better than some of our popular index total return calculators. ETFs (and mutual funds) are the most common ways to track an index, and they include fees and slow down dividend timing, making them more accurate for individual investors.

If you'd like to compare:

ETFs are relatively new when compared to common stocks and mutual funds. Still – at least for ETFs that pay dividends – we often see returns quoted out of context. When you buy VTI or DIA, don't only look at the price return on your fund. Be sure to factor in any additional shares you buy from the dividends you receive.

(Or, at least, know that you're spending the dividends.)

We hope you enjoyed the ETF total return calculator. *Use it in good health, and tell your friends!* Also, try the closed end fund return calculator.