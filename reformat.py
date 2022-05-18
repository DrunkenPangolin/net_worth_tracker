import numpy as np
import os
import pandas as pd
from accounts import *

APP_NAME = "csv_reformatter"

def reformat():
    # get name of folder in account directory, and access it
    os.chdir(os.path.join(".", "csv_data",'cash'))
    for account_name in os.listdir('.'):
        if ".csv" not in account_name:
            print(account_name)

            filepath = os.path.join('.', account_name)
            file_list = os.listdir(filepath)

            # account specific reformat to csv (if required)

            # merging csv files
            try:
                df = pd.concat(map(pd.read_csv,(os.path.join(filepath, file) for file in file_list)))
            except Exception as e:
                print(e)
                continue

            # dropping columns according to account based function
            df = globals()[account_name.lower().replace(" ", "_")](df)      # to be imported from accounts.py

            new_columns = [
                "date",
                "time",
                "name",
                "description",
                "type",
                "amount",
                "currency",
                "balance",
                "category",
            ]

            if 'time' not in list(df.columns):
                df['time'] = df.index
            df["date"] = pd.to_datetime(df.date, dayfirst=True)             # converting to date object, reading dd/mm/yyyy
            df = df.sort_values(['date','time']).reset_index()              # order by date, new index
            df = df.reindex(columns = new_columns)                          # adds & removes columns to create uniform output
            df.set_index('date', inplace=True)

            df.to_csv(account_name + ".csv")                                # write to file
    os.chdir('..')
    os.chdir('..')


if __name__ == "__main__":
    reformat()
