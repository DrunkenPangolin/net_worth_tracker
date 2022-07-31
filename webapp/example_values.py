# Basic Info
net_worth = 10500
nest_egg = 10000
total_assets = 10000
liabilities = 10000
open_credit = 10000
fi_number = 100000
available_credit = 10000
cash_credit = -1200
coast_fi = 10000
lean_fi = 30020

# Calculated info
fi_percentage = round((net_worth/fi_number)*100,1)

# Cards
card_net_worth = ('Net Worth',net_worth)
card_nest_egg = ('Nest Egg', nest_egg)
card_liabilities = ("LIABILITIES",liabilities)
card_open_credit = ("OPEN CREDIT",open_credit)
card_available_credit = ("AVAILABLE CREDIT",available_credit)
card_cash_credit = ("CASH VS CREDIT",cash_credit)
card_total_assets = ("Total Assets",total_assets)
card_fi_number = ("FI Number",fi_number)
card_fi_percentage = ("FI Percentage", fi_percentage)

# Milestones
milestone_first_100 =   ('First 100K',              100000,         round((net_worth/100000)*100, 1),           'date')
milestone_coast_fi =    ('Coast FI',                coast_fi,       round((net_worth/coast_fi)*100, 1),         'date')
milestone_half_fi =     ('Half FI',                 fi_number/2,    fi_percentage*2,                            'date')
milestone_lean_fi =     ('Lean FI',                 lean_fi,        round((net_worth/lean_fi)*100,1),           'date')
milestone_fi =          ('Financial Independence',  fi_number,      fi_percentage,                              'date')


# Expenses
table = [('Housing & Living','£8.63','£60.63','£262.75','£3153.00','11.70%'),('Health & Consumables','£11.95','£83.96','£363.83','£4366.00','16.20%'),('Transport','£0.64','£4.50','£19.50','£234.00','0.87%'),('Hobbies','£17.91','£125.83','£545.25','£6543.00','24.27%'),('Education','£1.80','£12.63','£54.75','£657.00','2.44%'),('Leisure & Discretionary','£9.37','£65.83','£285.25','£3423.00','12.70%'),('Travel','£20.96','£147.23','£638.00','£7656.00','28.40%'),('Work','£0.09','£0.65','£2.83','£34.00','0.13%'),('Income','£0.64','£4.50','£19.50','£234.00','0.87%'),('Transfer','£1.79','£12.58','£54.50','£654.00','2.43%')]
total = [("TOTAL", "£73.80", "£518.35", "£2246.17", "£26954.00", "100.00%")]

# Rolling averages
avg_earnings = ("","")
avg_savings = ("","")
avg_savings_rate = ("","")
investment_growth = ("","")
growth_rate = ("","")
avg_nw = ("","")
avg_fi_perc = ("","")
