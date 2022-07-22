# Documentation

## Roadmap
### Basic functionality and Accounts
- complete Flask app to basic standard using offline db saved in private repo
- add balances function to accounts on database (classes? csv files?)

### Portfolio tab and NW
- complete basic back end function, end of day balance for cash/credit accounts
- complete back end function for alternative assets (foreign currencies, stocks, material assets, crypto)
- complete back end function, net worth (cumulation of balances)
- feed net worth data to flask app, output data in values, graph, table
- complete back end functions applicable to Portfolio tab (breakdown and other informational data)
- feed portfolio data to flask app so that values, graphs, tables using JavaScript may be viewed on Portfolio and Dashboard tabs

### FI tab 
- set up back end functions for fi values where possible using manual fi value (100K and CoastFi milestones, 24 month averages )

### Expenses
- set up upload of csv files directly on flask app to database(s)
- set up manual expense categories
- set up back end function for expenses functionality
- 



## Bugs:
### CSS/HTML
- All CSS to do with forms
- No x to dismiss flash messages
- fix margins on FI tab for table
- fix margins on Accounts tab
- Would like a toggle for showing closed accounts
-

### Flask
- modal closes without any information output until reopen

### Database and Forms
- AccountForm/UpdateAccountForm requires input for Credit Limit (default=0), Benefit Expiry (default=None), Close Date
- UpdateAccountForm doesn't autofill selector fields eg. currency
- UpdateAccountForm doesn't validate account name if the same as original

### Python
- 



## Additional Notes

### Net Worth
- Basic net worth tracker using pandas
  - I am now happy importing from and storing dataframes to CSV files, though would like the app to work via a server and unsure if this would work as online storage, maybe SQL? Unsure, need to look into serialisation
  https://pandas.pydata.org/docs/reference/frame.html#serialization-io-conversion
- Require asset type and currency to be specified on each account
  - Cash account balances imported from CSV complete, need to figure out how to 
- Portfolio overview and total asset allocation viewed as percentage and absolute values in various currencies

### Expenses
- Multiple expense categories similar to Google Sheets

### Graphs
- NW over time with the same axes as in the Google Sheets (FI Number, NW, NE, Total Assets, Liabilities, Coast FI)

### Calculations
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
  - Coast/Alternative FI manual minimum target
    - Use this value for calculations?
  - Date of Birth
  - Life Expectancy (Could automate?)
  - Pension Accessibility Age (or could simply use a date if not using dob)
- FI %
- Drawdown Available
- % of Life Remaining Pre Pension	
- Net Worth Accessible Pre Pension	

### Separate Functions?
- Scrapers
  - Crypto values (CoinMarketCap, now using API - need to pull specific values from data)
  - Fund values (Morningstar?)
  - Stock values (Google? Yahoo?)
  - Accounts and Expenses (MoneyDashboard)
  - Currencies (https://pypi.org/project/forex-python/)
- Email 1 month/week before card benefits expire
- 

### Data
- Where to store? GitHub? Google Sheets?
- Possible backup data?
