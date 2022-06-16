import datetime
import pandas as pd
 
ACCOUNT_LIST = "account_list.csv"
account_name = 'Natwest DigiSaver'

# dropping columns according to account

f = open(ACCOUNT_LIST, "r")
for x in f.readlines()[1:]:
    y = x.split(',')
    if y[0] == account_name:
        columns = y[3].strip().split('; ')
        print(columns)
    