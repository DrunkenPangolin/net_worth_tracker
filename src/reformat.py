from cmath import nan
import numpy as np
import os
import pandas as pd
from accounts import *

APP_NAME = "csv_reformatter"

def reformat():
    """designed to reformat csv files so that all are uniform"""
    
    ACCOUNT_LIST = "account_list.csv"
    DESIRED_COLUMNS = [
        "date",
        "time",
        "name",
        "description",
        "type",
        "amount",
        "balance",
        "currency",
        "category",
    ]

    # get name of folder in account directory, and access it
    dir = "csv_data"
    for account_name in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, account_name)):
            print(account_name)

            path = os.path.join(dir, account_name)
            file_list = os.listdir(path)

            # account specific reformat to csv (if required)
  #          try:
   #             globals()[account_name.lower().replace(" ", "_")]      # to be imported from accounts.py
    #        except Exception as e:
     #           print(str(e) + " function not found")
      #          continue

            # merging csv files
            try:
                df = pd.concat(map(pd.read_csv,(os.path.join(path, x) for x in file_list)))
            except Exception as e:
                print(e)
                continue

            # renaming columns according to account
            cols = []
            try:
                f = open(ACCOUNT_LIST, "r")
                for x in f.readlines()[1:]:
                    y = x.split(',')
                    if y[0] == account_name:
                        account_data = y[3].split(';')
                        if 'date' not in account_data:
                                continue
                        for heading in account_data:
                            cols.append(heading.strip())
            except Exception as e:
                print(str(e) + " function not found")
                continue
            df.columns = cols


            # dropping unneeded columns
            if 'time' not in list(df.columns):
                df['time'] = df.index
            df["date"] = pd.to_datetime(df.date, dayfirst=True)             # converting to date object, reading dd/mm/yyyy
            df = df.sort_values(['date','time'])                            # order by date
            df = df.reindex(columns = DESIRED_COLUMNS)                      # adds & removes columns to create uniform output
            df = df.drop_duplicates()
            df.set_index('date', inplace=True)
            df['currency'] = np.where(df['currency'].isna(), accounts().loc[account_name,'currency'], df['currency'])

            print(df)
            df.to_csv(os.path.join(dir,account_name + ".csv"))              # write to file
 

if __name__ == "__main__":
    reformat()
