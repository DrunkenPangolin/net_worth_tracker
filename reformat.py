import numpy as np
import os
import pandas as pd

def change_cat(df:pd.DataFrame, new_category: str, column: str, criteria: str) -> pd.DataFrame:
    df['category'] = np.where(df[column].str.contains(criteria), new_category, df['category'])


def aj_bell(df:pd.DataFrame):
    return df

def paypal(df:pd.DataFrame):
    df = df.drop(columns=["Time zone", 'Gross', 'Fee', 'Receipt ID', 'Tip'])
    return df

def premium_bonds(df:pd.DataFrame):
    df = df.drop(columns=["Action"])
    df.insert(1,'name', pd.NaT)
    df.insert(3, 'type', pd.NaT)
    df['category'] = 'Internal'
    change_cat(df,'Interest','Description','prize')
    df['Amount'] = np.where(df['Description'].str.contains('deposit|prize'), df['Amount'], df['Amount']*(-1))
    return df

def starling(df:pd.DataFrame):
    df = df.drop(columns=["Notes"])
    # changing categories
    #change_cat(df,'Investments','name','Vanguard|AJ Bell|Freetrade|212|Halifax Share Dealing')
    #change_cat(df,'Internal','name',"Chase|Virgin Money|TSB|Royal Bank of Scotland|Tandem|Me -|Samuel Price|Sainsbury's Bank|Revolut|New Day|Nationwide|Halifax Cards")
    #change_cat(df,'Interest','description','Interest')
    return df





def reformat():
    # get name of folder in account directory, and access it
    directory = os.path.join('.','csv_data')
    for account_name in os.listdir(directory):
        if '.csv' not in account_name:
            print(account_name)

            filepath = os.path.join(directory,account_name)
            file_list = os.listdir(filepath)


            # account specific reformat to csv (if required)


            # merging csv files
            try:
                df = pd.concat(map(pd.read_csv,(os.path.join(filepath,file) for file in file_list)))
            except Exception as e:
                print(e)
                continue
            
            # dropping columns according to account based function
            df = globals()[account_name.lower().replace(' ','_')](df)

            try:
                # renaming headers
                df.columns = ['date','name','description','type','amount','balance','category']

                df["date"] = pd.to_datetime(df.date, dayfirst=True)         # converting to date object, reading dd/mm/yyyy
                df = df.sort_values(["date"]).reset_index()                 # order by date, new index
                df = df.drop(columns=["index"])                             # dropping old index
            except Exception as e:
                print(e)

            df.to_csv(os.path.join(directory,account_name+'.csv'))          # write to file


if __name__ == '__main__':
    reformat()