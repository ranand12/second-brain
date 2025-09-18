# How I get options data for free

Column: https://www.freecodecamp.org/news/how-i-get-options-data-for-free-fba22d395cc8/amp/
Processed: No
created on: January 1, 2022 7:48 AM
topics: money, python, tech-stuff

![](How%20I%20get%20options%20data%20for%20free%20478aac92c819412d87c6d0bb7a49fc39/08B9koPyETFCwVvO6.png)

by Harry Sauers

### An introduction to web scraping for finance

Ever wished you could access historical options data, but got blocked by a paywall? What if you just want it for research, fun, or to develop a personal trading strategy?

In this tutorial, you’ll learn how to use Python and BeautifulSoup to scrape financial data from the Web and build your own dataset.

### **Getting Started**

You should have at least a working knowledge of Python and Web technologies before beginning this tutorial. To build these up, I highly recommend checking out a site like [codecademy](https://www.codecademy.com/) to learn new skills or brush up on old ones.

First, let’s spin up your favorite IDE. Normally, I use [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html) but, for a quick script like this [Repl.it](https://repl.it/) will do the job too. Add a quick print (“Hello world”) to ensure your environment is set up correctly.

Now we need to figure out a data source.

Unfortunately, [Cboe’s awesome options chain data](http://www.cboe.com/delayedquote/quote-table) is pretty locked down, even for current delayed quotes. Luckily, Yahoo Finance has solid enough options data [here](https://finance.yahoo.com/quote/SPY/options?p=SPY). We’ll use it for this tutorial, as web scrapers often need some content awareness, but it is easily adaptable for any data source you want.

### **Dependencies**

We don’t need many external dependencies. We just need the Requests and BeautifulSoup modules in Python. Add these at the top of your program:

```
from bs4 import BeautifulSoupimport requests
```

Create a `main` method:

```
def main():  print(“Hello World!”)if __name__ == “__main__”:  main()
```

### Scraping HTML

Now you’re ready to start scraping! Inside `main()`, add these lines to fetch the page’s full `HTML`:

```
data_url = “https://finance.yahoo.com/quote/SPY/options"data_html = requests.get(data_url).contentprint(data_html)
```

This fetches the page’s full `HTML` content, so we can find the data we want in it. Feel free to give it a run and observe the output.

Feel free to comment out print statements as you go — these are just there to help you understand what the program is doing at any given step.

BeautifulSoup is the perfect tool for working with `HTML` data in Python. Let’s narrow down the `HTML` to just the options pricing tables so we can better understand it:

```
 content = BeautifulSoup(data_html, “html.parser”) # print(content)
```

```
 options_tables = content.find_all(“table”) print(options_tables)
```

That’s still quite a bit of `HTML` — we can’t get much out of that, and Yahoo’s code isn’t the most friendly to web scrapers. Let’s break it down into two tables, for calls and puts:

```
 options_tables = [] tables = content.find_all(“table”) for i in range(0, len(content.find_all(“table”))):   options_tables.append(tables[i])
```

```
 print(options_tables)
```

Yahoo’s data contains options that are pretty deep in- and out-of-the-money, which might be great for certain purposes. I’m only interested in near-the-money options, namely the two calls and two puts closest to the current price.

Let’s find these, using BeautifulSoup and Yahoo’s differential table entries for in-the-money and out-of-the-money options:

```
expiration = datetime.datetime.fromtimestamp(int(datestamp)).strftime(“%Y-%m-%d”)
```

```
calls = options_tables[0].find_all(“tr”)[1:] # first row is header
```

```
itm_calls = []otm_calls = []
```

```
for call_option in calls:    if “in-the-money” in str(call_option):  itm_calls.append(call_option)  else:    otm_calls.append(call_option)
```

```
itm_call = itm_calls[-1]otm_call = otm_calls[0]
```

```
print(str(itm_call) + “ \n\n “ + str(otm_call))
```

Now, we have the table entries for the two options nearest to the money in `HTML`. Let’s scrape the pricing data, volume, and implied volatility from the first call option:

```
 itm_call_data = [] for td in BeautifulSoup(str(itm_call), “html.parser”).find_all(“td”):   itm_call_data.append(td.text)
```

```
print(itm_call_data)
```

```
itm_call_info = {‘contract’: itm_call_data[0], ‘strike’: itm_call_data[2], ‘last’: itm_call_data[3],  ‘bid’: itm_call_data[4], ‘ask’: itm_call_data[5], ‘volume’: itm_call_data[8], ‘iv’: itm_call_data[10]}
```

```
print(itm_call_info)
```

Adapt this code for the next call option:

```
# otm callotm_call_data = []for td in BeautifulSoup(str(otm_call), “html.parser”).find_all(“td”):  otm_call_data.append(td.text)
```

```
# print(otm_call_data)
```

```
otm_call_info = {‘contract’: otm_call_data[0], ‘strike’: otm_call_data[2], ‘last’: otm_call_data[3],  ‘bid’: otm_call_data[4], ‘ask’: otm_call_data[5], ‘volume’: otm_call_data[8], ‘iv’: otm_call_data[10]}
```

```
print(otm_call_info)
```

Give your program a run!

You now have dictionaries of the two near-the-money call options. It’s enough just to scrape the table of put options for this same data:

```
puts = options_tables[1].find_all("tr")[1:]  # first row is header
```

```
itm_puts = []  otm_puts = []
```

```
for put_option in puts:    if "in-the-money" in str(put_option):      itm_puts.append(put_option)    else:      otm_puts.append(put_option)
```

```
itm_put = itm_puts[0]  otm_put = otm_puts[-1]
```

```
# print(str(itm_put) + " \n\n " + str(otm_put) + "\n\n")
```

```
itm_put_data = []  for td in BeautifulSoup(str(itm_put), "html.parser").find_all("td"):    itm_put_data.append(td.text)
```

```
# print(itm_put_data)
```

```
itm_put_info = {'contract': itm_put_data[0],                  'last_trade': itm_put_data[1][:10],                  'strike': itm_put_data[2], 'last': itm_put_data[3],                   'bid': itm_put_data[4], 'ask': itm_put_data[5], 'volume': itm_put_data[8], 'iv': itm_put_data[10]}
```

```
# print(itm_put_info)
```

```
# otm put  otm_put_data = []  for td in BeautifulSoup(str(otm_put), "html.parser").find_all("td"):    otm_put_data.append(td.text)
```

```
# print(otm_put_data)
```

```
otm_put_info = {'contract': otm_put_data[0],                  'last_trade': otm_put_data[1][:10],                  'strike': otm_put_data[2], 'last': otm_put_data[3],                   'bid': otm_put_data[4], 'ask': otm_put_data[5], 'volume': otm_put_data[8], 'iv': otm_put_data[10]}
```

Congratulations! You just scraped data for all near-the-money options of the S&P 500 ETF, and can view them like this:

```
 print("\n\n") print(itm_call_info) print(otm_call_info) print(itm_put_info) print(otm_put_info)
```

Give your program a run — you should get data like this printed to the console:

```
{‘contract’: ‘SPY190417C00289000’, ‘last_trade’: ‘2019–04–15’, ‘strike’: ‘289.00’, ‘last’: ‘1.46’, ‘bid’: ‘1.48’, ‘ask’: ‘1.50’, ‘volume’: ‘4,646’, ‘iv’: ‘8.94%’}{‘contract’: ‘SPY190417C00290000’, ‘last_trade’: ‘2019–04–15’, ‘strike’: ‘290.00’, ‘last’: ‘0.80’, ‘bid’: ‘0.82’, ‘ask’: ‘0.83’, ‘volume’: ‘38,491’, ‘iv’: ‘8.06%’}{‘contract’: ‘SPY190417P00290000’, ‘last_trade’: ‘2019–04–15’, ‘strike’: ‘290.00’, ‘last’: ‘0.77’, ‘bid’: ‘0.75’, ‘ask’: ‘0.78’, ‘volume’: ‘11,310’, ‘iv’: ‘7.30%’}{‘contract’: ‘SPY190417P00289000’, ‘last_trade’: ‘2019–04–15’, ‘strike’: ‘289.00’, ‘last’: ‘0.41’, ‘bid’: ‘0.40’, ‘ask’: ‘0.42’, ‘volume’: ‘44,319’, ‘iv’: ‘7.79%’}
```

### Setting up recurring data collection

Yahoo, by default, only returns the options for the date you specify. It’s this part of the URL: [https://finance.yahoo.com/quote/SPY/options?date=**1555459200**](https://finance.yahoo.com/quote/SPY/options?date=1555459200)

This is a Unix timestamp, so we’ll need to generate or scrape one, rather than hardcoding it in our program.

Add some dependencies:

```
import datetime, time
```

Let’s write a quick script to generate and verify a Unix timestamp for our next set of options:

```
def get_datestamp():  options_url = “https://finance.yahoo.com/quote/SPY/options?date="  today = int(time.time())  # print(today)  date = datetime.datetime.fromtimestamp(today)  yy = date.year  mm = date.month  dd = date.day
```

The above code holds the base URL of the page we are scraping and generates a `datetime.date` object for us to use in the future.

Let’s increment this date by one day, so we don’t get options that have already expired.

```
dd += 1
```

Now, we need to convert it back into a Unix timestamp and make sure it’s a valid date for options contracts:

```
 options_day = datetime.date(yy, mm, dd) datestamp = int(time.mktime(options_day.timetuple())) # print(datestamp) # print(datetime.datetime.fromtimestamp(options_stamp))
```

```
 # vet timestamp, then return if valid for i in range(0, 7):   test_req = requests.get(options_url + str(datestamp)).content   content = BeautifulSoup(test_req, “html.parser”)   # print(content)   tables = content.find_all(“table”)
```

```
 if tables != []:   # print(datestamp)   return str(datestamp) else:   # print(“Bad datestamp!”)   dd += 1   options_day = datetime.date(yy, mm, dd)   datestamp = int(time.mktime(options_day.timetuple()))  return str(-1)
```

Let’s adapt our `fetch_options` method to use a dynamic timestamp to fetch options data, rather than whatever Yahoo wants to give us as the default.

Change this line:

```
data_url = “https://finance.yahoo.com/quote/SPY/options"
```

To this:

```
datestamp = get_datestamp()data_url = “https://finance.yahoo.com/quote/SPY/options?date=" + datestamp
```

Congratulations! You just scraped real-world options data from the web.

Now we need to do some simple file I/O and set up a timer to record this data each day after market close.

### Improving the program

Rename `main()` to `fetch_options()` and add these lines to the bottom:

```
options_list = {‘calls’: {‘itm’: itm_call_info, ‘otm’: otm_call_info}, ‘puts’: {‘itm’: itm_put_info, ‘otm’: otm_put_info}, ‘date’: datetime.date.fromtimestamp(time.time()).strftime(“%Y-%m-%d”)}return options_list
```

Create a new method called `schedule()`. We’ll use this to control when we scrape for options, every twenty-four hours after market close. Add this code to schedule our first job at the next market close:

```
from apscheduler.schedulers.background import BackgroundScheduler
```

```
scheduler = BackgroundScheduler()
```

```
def schedule():  scheduler.add_job(func=run, trigger=”date”, run_date = datetime.datetime.now())  scheduler.start()
```

In your `if __name__ == “__main__”:` statement, delete `main()` and add a call to `schedule()` to set up your first scheduled job.

Create another method called `run()`. This is where we’ll handle the bulk of our operations, including actually saving the market data. Add this to the body of `run()`:

```
  today = int(time.time()) date = datetime.datetime.fromtimestamp(today) yy = date.year mm = date.month dd = date.day
```

```
 # must use 12:30 for Unix time instead of 4:30 NY time next_close = datetime.datetime(yy, mm, dd, 12, 30)
```

```
 # do operations here “”” This is where we’ll write our last bit of code. “””
```

```
 # schedule next job scheduler.add_job(func=run, trigger=”date”, run_date = next_close)
```

```
 print(“Job scheduled! | “ + str(next_close))
```

This lets our code call itself in the future, so we can just put it on a server and build up our options data each day. Add this code to actually fetch data under `“”” This is where we’ll write our last bit of code. “””`

```
options = {}
```

```
 # ensures option data doesn’t break the program if internet is out try:   if next_close > datetime.datetime.now():     print(“Market is still open! Waiting until after close…”)   else:     # ensures program was run after market hours     if next_close < datetime.datetime.now():      dd += 1       next_close = datetime.datetime(yy, mm, dd, 12, 30)       options = fetch_options()       print(options)       # write to file       write_to_csv(options)except:  print(“Check your connection and try again.”)
```

### Saving data

You may have noticed that `write_to_csv` isn’t implemented yet. No worries — let’s take care of that here:

```
def write_to_csv(options_data):  import csv  with open(‘options.csv’, ‘a’, newline=’\n’) as csvfile:  spamwriter = csv.writer(csvfile, delimiter=’,’)  spamwriter.writerow([str(options_data)])
```

### **Cleaning up**

As options contracts are time-sensitive, we might want to add a field for their expiration date. This capability is not included in the raw HTML we scraped.

Add this line of code to save and format the expiration date towards the top of `fetch_options()`:

```
expiration =  datetime.datetime.fromtimestamp(int(get_datestamp())).strftime("%Y-%m-%d")
```

Add `‘expiration’: expiration` to the end of each `option_info` dictionary like so:

```
itm_call_info = {'contract': itm_call_data[0],  'strike': itm_call_data[2], 'last': itm_call_data[3],   'bid': itm_call_data[4], 'ask': itm_call_data[5], 'volume': itm_call_data[8], 'iv': itm_call_data[10], 'expiration': expiration}
```

Give your new program a run — it’ll scrape the latest options data and write it to a .csv file as a string representation of a dictionary. The .csv file will be ready to be parsed by a backtesting program or served to users through a webapp. Congratulations!