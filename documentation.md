#Documentation

Bugs:
CSS
- Drop down box in menu is too high (adjusted correctly when name isn't present)
- Drop down box in menu drops left, on phone view this is off screen
- All CSS to do with forms
- No x to quit on flash messages

Flask
- FlaskForm doesn't validate if there is an additional section in form that doesn't appear in page, I would like to use the same form for updates as well as initial adding to database

Database
- AccountForm requires input for Credit Limit (default=0) and Benefit Expiry (default=None)

Python
- 














Front end - Flask with HTML via Bootstrap

Back end functions - Python

Net Worth
- Basic net worth tracker using pandas
  - I am now happy importing from and storing dataframes to CSV files (good for debugging too), though would like the app to work via a server and unsure if this would work as online storage, maybe SQL? Unsure
  https://pandas.pydata.org/docs/reference/frame.html#serialization-io-conversion
- Require asset type and currency to be specified on each account
  - Cash account balances imported from CSV complete, need to figure out how to 
- Portfolio overview and total asset allocation viewed as percentage and absolute values in various currencies

Expenses
- Multiple expense categories similar to Google Sheets

Graphs
- NW over time with the same axes as in the Google Sheets (FI Number, NW, NE, Total Assets, Liabilities, Coast FI)

Calculations
- Calculations over adjustable time period (2 years)
- Average monthly/yearly figures
  - Earnings
  - Savings
  - Investment Growth
  - Growth Rate
  - NW Change
  - FI Percentage Change
- FI date
- Milestones and dates
- Settings page
  - Safe Withdrawal Rate	
  - Predicted Annual Growth Rate
  - Rolling Average
  - Coast/Alternative FI manual target
    - Use this value for calculations?
  - Date of Birth
  - Life Expectancy (Could automate?)
  - Pension Accessibility Age
- FI %
- Drawdown Available
- % of Life Remaining Pre Pension	
- Net Worth Accessible Pre Pension	

Separate Functions
- Scrapers
  - Crypto values (CoinMarketCap, now using API - need to pull specific values from data)
  - Fund values (Morningstar?)
  - Stock values (Google? Yahoo?)
  - Accounts and Expenses (MoneyDashboard)
  - Currencies (https://pypi.org/project/forex-python/)
- Email 1 month/week before card benefits expire
- 

Data
- Where to store? GitHub? Google Sheets?
- Possible backup data?

Automation
- Pull account balances and expenses from MoneyDashboard
- Pull currency exchange rates from Google(?), these should be individual for each date
- 

Implemented:
`init.py`
- sets up the necessary folder system and creates account_list.csv

`reformat.py`
- unifies and reformats the csv files from each bank into a uniform format
- imports functions from `accounts.py` for difficult/non CSVs

`accounts.py`
- 

`balances.py`
- converts pandas rows/columns to desired currency
- strips csv file to only date and end of day balance
- unify all balance sheet in folder


Yet to implement:


Useful notes?:
https://streamlit.io