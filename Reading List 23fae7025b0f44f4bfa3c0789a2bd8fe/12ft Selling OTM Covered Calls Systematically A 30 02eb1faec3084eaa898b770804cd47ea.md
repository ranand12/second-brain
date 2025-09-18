# 12ft | Selling OTM Covered Calls Systematically: A 30-Year Backtest | Seeking Alpha

Column: https://12ft.io/proxy?q=https://seekingalpha.com/article/4353418-selling-otm-covered-calls-systematically-30-year-backtest
Processed: No
created on: November 1, 2022 8:59 PM
topics: money

While selling out of the money (OTM) covered calls on stocks is a nice way to generate income most of the time, but in order to use any strategy confidently, we need to understand how they work all of the time. But, for the more mathematically inclined, this poses an optimization challenge.

The question is: how far out of the money should be these contracts to maximize the risk/reward tradeoff of this activity? The knee-jerk answer of "just make the strike about 10% higher than the current index price" might sound reasonable, but falls short: the volatility of a stock changes over time. 10% might be appropriate for a quiet time of consolidation, but completely inappropriate for a bull market price rise.

## **Conceptualizing Strike Prices Using Standard Deviations OTM**

I propose that the most logical way to measure moneyness is in terms of multiples of standard deviations of volatility. I'll give you the equation and walk you through two examples. Feel free to skip this if you're all set on this math.

For a stock price P, volatility σ, strike price K that is n standard deviations above/below P, and option expiration of t, the equation that gives the option strike price K is:

Suppose that a stock has a current price of $100 and a volatility of 20%:

The strike price on a 1 standard deviation out of the money call with expiration 91 days (1/4 of a year) is:

The strike price on a 0.5 standard deviation OTM call with expiration 30 days (1/12 of a year) is:

## **Simulation Conditions**

*Our goal is to understand this: If I sell options on a monthly basis, what is the best standard deviation I should consistently use to calculate my strike price for each contract so that I maximize my portfolio risk/return characteristics?*

For the purposes of this article, we will focus on S&P 500 options. For the purposes of simplicity, we will sell enough 28-day European contracts with a notional value equal to the entire S&P 500 holding. (So, if I held 1000 SPX shares - if they existed - I would sell 10 SPX contracts of calls every 28 days.) As soon as the previous contract is settled, the next contract is bought on the same day.

As a retail investor, my access to options information is limited, so I set up a spreadsheet that could take time series of historical VIX data (30-day forward volatility on the S&P 500, taken from Yahoo Finance), Fed Funds Rate (risk free interest rate, publicly available), and historical SPX values (from Yahoo Finance), and use the Black-Scholes formula to estimate the historical option price for every historical date in the calculation.

I assumed that the portfolio was 100% composed of the S&P 500 index. Whenever each contract was sold, the proceeds were added to the portfolio's value. Whenever an option expired in the money, the payout was subtracted from the portfolio's value.

Daily VIX figures were used directly as the volatility inputs into calculating strike prices.

No cash was added to or removed from the portfolio, and all profits were reinvested. All portfolios began with $10,000 on Jan 1990 and assume that fractional shares and options are possible.

## **Simulation Results**

The best strategy was to sell covered calls with strikes 0.5 standard deviations OTM. This line is drawn in light blue, followed by 0.75, 1, 1.25, and 1.5 standard deviations.

Note that the most "greedy" strategies (ATM and 0.25 standard deviations) underperformed in total return.

![](12ft%20Selling%20OTM%20Covered%20Calls%20Systematically%20A%2030%2002eb1faec3084eaa898b770804cd47ea/39844506-15917580063197901.png)

The following is a table that summarizes the CAGR and volatility for each strategy, from Jan 1990 to May 2020:

| Number of Standard Deviations | CAGR (%) | Volatility (%) |
| --- | --- | --- |
| S&P 500 Alone | 7.081 | 15.369 |
| 1.50 | 9.854 | 15.166 |
| 1.25 | 11.286 | 14.935 |
| 1.00 | 13.058 | 14.492 |
| 0.75 | 14.729 | 13.632 |
| 0.50 | 15.466 | 12.233 |
| 0.25 | 15.089 | 10.451 |
| 0.00 | 13.691 | 8.506 |

Interestingly, portfolio volatility decreased as the covered calls had strikes approaching ATM values. Why should this be so? We'll see that in the next series of charts, but here's my answer. Options become more valuable when volatility rises. Usually, high stock market volatility means that the stock is going down. *Proceeds from covered calls are high exactly when stocks are plunging,* so there is a dampening effect on downside volatility.

Just when you think that you'll start selling covered calls with strike prices 0.50 standard deviations OTM, consider this: how painful is such a strategy to execute? What are the payouts when options expire in the money?

## **Option Premiums & Payouts By Strategy**

Here are four charts that show the option premiums and payouts for four strategies: 1.50, 1.00, 0.50, and 0.00 standard deviations. All numbers are scaled to assume that the portfolio consists of exactly one S&P 500 index share - if it existed.

![](12ft%20Selling%20OTM%20Covered%20Calls%20Systematically%20A%2030%2002eb1faec3084eaa898b770804cd47ea/39844506-15917580520987132.png)

![](12ft%20Selling%20OTM%20Covered%20Calls%20Systematically%20A%2030%2002eb1faec3084eaa898b770804cd47ea/39844506-1591758065500783.png)

![](12ft%20Selling%20OTM%20Covered%20Calls%20Systematically%20A%2030%2002eb1faec3084eaa898b770804cd47ea/39844506-15917580783307912.png)

![](12ft%20Selling%20OTM%20Covered%20Calls%20Systematically%20A%2030%2002eb1faec3084eaa898b770804cd47ea/39844506-1591758096481781.png)

Two trends are apparent as the strategy becomes more and more conservative. Option premiums decrease the further out you go, and the fraction of sold calls that are exercised at a loss decreases.

Take a look back at the 0.5 standard deviation OTM strategy. The backtest showed that this strategy creates the greatest expected portfolio yield. But the payouts from options that expire in the money are very substantial. Do you have the intestinal strength to pursue that sort of strategy?

## **Problems with this simulation**

To keep the calculations simple, this simulation assumed several things that cannot be expected of or are unrealistic in the real world:

- Option prices precisely follow the Black-Scholes model. Because of the fat-tailed nature of the distribution of stock returns, I would believe that real OTM call prices would be higher than those predicted by the Black-Scholes model.
- Fractional option contracts can be traded. OR, that the portfolio is so large that shares that cannot be used to cover a call are insignificant.
- The model assumed European options. In reality, SPX options are European but SPY options are American. Since American options should theoretically be slightly more expensive than European options, a strategy conducted with American options should have a bigger premium income stream and also a higher probability & quantity of payouts when the calls are exercised.
- The model assumes that the options are cash settled. If they are settled with the underlying (as are options on SPY), the price of the underlying moves from between when the option is exercised and the cash proceeds are used to repurchase the underlying.
- The BIG one: these simulations did not account for commissions and taxes. Commissions can be minimized by picking an appropriate broker (e.g. Interactive Brokers). Taxes can be troublesome - exercised calls can force you to sell an appreciated holding and force you to pay capital gains tax. Keeping track of this and setting aside cash to pay these taxes can be a nightmare. You also pay income taxes on all the collected option premiums. But, none of the tax headaches happen if you have a tax-advantaged account that lets you trade options.

Have you tried this sort of strategy before? How did it go? I'd like to hear from you in the comments.

**Disclosure:** I/we have no positions in any stocks mentioned, and no plans to initiate any positions within the next 72 hours. I wrote this article myself, and it expresses my own opinions. I am not receiving compensation for it (other than from Seeking Alpha). I have no business relationship with any company whose stock is mentioned in this article.