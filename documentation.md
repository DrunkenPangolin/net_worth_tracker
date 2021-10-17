#Documentation

Implemented
- No code written... yet!

Plan
Net Worth
- Basic net worth tracker involving a pandas dataframe of different accounts (need to find out how to save dataframes to file https://stackoverflow.com/questions/17098654/how-to-reversibly-store-and-load-a-pandas-dataframe-to-from-disk)
- Require asset type and currency to be specified on each account
- Date should be independent variable and can track as often or as little as required
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
  - Currencies (Google? XE?)
- 

Data
- Where to store? GitHub? Google Sheets?
- Possible backup data?

Automation
- Pull account balances and expenses from MoneyDashboard
- Pull currency exchange rates from Google(?), these should be individual for each date
- 
