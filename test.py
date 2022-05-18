import datetime
import pandas as pd
 
df = pd.read_csv('account_list.csv')
print(df)
df.set_index('account_name', inplace=True)

df = df.loc['Starling','currency']
print(df)