import datetime
import pandas as pd
 
todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date, periods=5, freq='D')
 
columns = []
 
df = pd.DataFrame(index=index, columns=columns)
 
print(df)