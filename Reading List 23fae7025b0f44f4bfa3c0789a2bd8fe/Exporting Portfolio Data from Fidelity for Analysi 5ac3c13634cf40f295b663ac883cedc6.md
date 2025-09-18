# Exporting Portfolio Data from Fidelity for Analysis | by Will Keefe | InsiderFinance Wire

Column: https://wire.insiderfinance.io/exporting-portfolio-data-from-fidelity-for-analysis-d212ac83ad99
Processed: No
created on: December 25, 2021 8:07 AM
topics: money, python, tech-stuff

Many American’s use Fidelity’s brokerage services for their independent investing accounts, 401Ks, and Roth IRAs. Fidelity has some great visualization tools built into their platform but does not have any user-friendly external connections customizable to their clients, although you can download your portfolio as a CSV in a non-automated fashion. Some websites such as [Yahoo Finance](https://finance.yahoo.com/portfolios) allow users to connect their accounts to visualize their current portfolio holdings, but even then the dashboarding capabilities are limited by Yahoo’s platform, and some services are even blocked behind a paywall.

A do-it-yourself alternative to get up-to-date portfolio holding daily is to use [Selenium](https://www.selenium.dev/) and a script written in a language such as Python to automate downloading data. Then, users can either open the content within Excel or take advantage of the many open source libraries available in Python for tracking asset fundamentals or leveraging advanced technical analysis.

![](Exporting%20Portfolio%20Data%20from%20Fidelity%20for%20Analysi%205ac3c13634cf40f295b663ac883cedc6/1t7tzqMxa9PhPC3A_-EWMjA.png)

![](Exporting%20Portfolio%20Data%20from%20Fidelity%20for%20Analysi%205ac3c13634cf40f295b663ac883cedc6/1t7tzqMxa9PhPC3A_-EWMjA%201.png)

Screen capture of the current Selenium website with multiple download links.

Within the scope of this article, we will go over how Selenium scripts are recorded, how to implement that code within a Python script, and how to export a downloaded portfolio to a Pandas data frame within Python.

As background on Selenium, this software is freely available for user interface testing. During the software development lifecycle, the best websites and services are robustly tested to handle a variety of inputs and correct mistakes as they are encountered. Selenium is a tool for automating that process. Testing and completing lengthy forms or website practices for example take one user hours due to all of the repetitive keystrokes and mouse clicks, but a robot running on a server mere moments. For our case, we will be running one of these tests only once; we will be opening a new window, logging into Fidelity, navigating to our portfolio holdings, interacting with a button to download a copy of our portfolio, and logging out and closing the window. As a bonus at the end, I am also including additional elements to our script to move the copied file to a location other than our downloads folder (the default location), and how to open the content as a Pandas data frame for further analysis.

The first step complete to develop our testing script was to install the [Selenium IDE](https://chrome.google.com/webstore/detail/selenium-ide/) as an extension for our web browser, in my case Chrome. A series of drivers will also be needed, with installation instructions found [here](https://selenium-python.readthedocs.io/installation.html).

Once Selenium is installed, the script can be recorded from the extension and is as simple as recording a macro within Excel.

![](Exporting%20Portfolio%20Data%20from%20Fidelity%20for%20Analysi%205ac3c13634cf40f295b663ac883cedc6/1G1TktJVS3Wp0GzYC4_5dwg.png)

Screenshot of Selenium IDE running within Chrome

We create a new project name, enter the Fidelity log-in page as our base URL, and then simply navigate to our portfolio, click the download link, log out, and close the window. Performing these tasks on our own is easy, and fortunately, the IDE handles the hard work of writing the code for us. To get our Python scripts out of the IDE and into a file users should right-click on the test name seen above (Untitled* in the photo), and export as a Python pytest. This process could be repeated with any other brokerage or site as well if there are similar operations that can be repeated.

A lot of the code provided by the IDE will not be used. For simplicity’s sake below is the working code that can be used to routinely perform these tasks.

```
import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time#Configure and launch driver for selenium data pull from Fidelity
driver = webdriver.Chrome()
vars = {}
driver.get("https://www.fidelity.com/")
driver.set_window_size(1587, 942)
driver.find_element(By.ID, "userId-input").click()
driver.find_element(By.ID, "userId-input").send_keys("USERNAME")
driver.find_element(By.ID, "password").send_keys("PASSWORD")
driver.find_element(By.ID, "fs-login-button").click()
#Wait for enough time to web page to render
time.sleep(5)
driver.find_element(By.ID, "tab-2").click()
#Wait for enough time to web page to render
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".posweb-grid_top-download-button").click()
#Wait for enough time to web page to render
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".pntlt > .pnlogin > .pnls > a").click()
driver.quit()
```

Note that we also imported the Python time library. Our new script may execute so quickly some components may not have loaded in depending on internet download speeds. The sleep values can be modified as needed, and if using this code don’t forget to enter your USERNAME and PASSWORD!

Now you have a newly downloaded copy of your portfolio in your downloads folder. What’s next? The choice is yours.

Below is another snippet of code for moving your CSV to a different folder, and opening it as a Pandas data frame. From there, the data can be manipulated up to your preferences. Another great library available for use is [yfinance](https://pypi.org/project/yfinance/) and integrating it will allow you to investigate a plethora of information about each of your assets.

```
#Get todays date to add to the path
today = date.today()
todayDateString = today.strftime("%b-%d-%Y")
path = "Portfolio_Positions_" + todayDateString + ".csv"
oPath = "/Users/USER/Downloads/" + path
dPath = "/Users/USER/Documents/YOURFOLDER/" + path
shutil.move(oPath,dPath)import pandas as pd
df = pd.read_csv(dPath)
#Drop the last 3 rows which are disclaimers
df.drop(df.tail(3).index,inplace=True)
```

You now have a data frame with all of your asset data from Fidelity. Please feel free to check out my other articles on how to manipulate this data, and use it in analysis!

DISCLAIMER — This is not financial advice nor am I a financial professional. Please be responsible when making financial decisions.