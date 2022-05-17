import numpy as np
import os
import pandas as pd


def change_cat(df: pd.DataFrame, new_category: str, column: str, criteria: str) -> pd.DataFrame:
    df["category"] = np.where(df[column].str.contains(criteria), new_category, df["category"])


def paypal(df: pd.DataFrame):
    df.columns = [
        "date",
        "time",
        "time_zone",
        "name",
        "type",
        "status",
        "currency",
        "gross",
        "fee",
        "net",
        "receipt_id",
        "balance",
        "tip",
    ]
    return df


def premium_bonds(df: pd.DataFrame):
    df.columns = [
        "date",
        "description",
        "amount",
        "balance",
        "action"
    ]
    df["category"] = "internal"
    change_cat(df, "interest", "description", "prize")
    df["amount"] = np.where(
        df["description"].str.contains("deposit|prize"),
        df["amount"],
        df["amount"] * (-1),
    )
    df = df.sort_index(ascending=False).reset_index()
    return df


def starling(df: pd.DataFrame):
    df.columns = [
        "date",
        "name",
        "description",
        "type",
        "amount",
        "balance",
        "category",
        "notes",
    ]

    # changing categories
    change_cat(df, "investments", "name",
        """
        Vanguard|
        AJ Bell|
        Freetrade|
        212|
        Halifax Share Dealing
        """,
    )
    change_cat(df, "internal", "name",
        """
        Chase|
        Virgin Money|
        TSB|
        Royal Bank of Scotland|
        Tandem|
        Me -|
        Samuel Price|
        Sainsbury's Bank|
        Revolut|
        New Day|
        Nationwide|
        Halifax Cards
        """
    )
    change_cat(df, "interest", "description", "nterest")
    return df


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
            df = globals()[account_name.lower().replace(" ", "_")](df)

            new_columns = [
                "date",
                "time",
                "name",
                "description",
                "type",
                "amount",
                "balance",
                "category",
            ]

            if 'time' not in list(df.columns):
                df['time'] = df.index
            df["date"] = pd.to_datetime(df.date, dayfirst=True)             # converting to date object, reading dd/mm/yyyy
            df = df.sort_values(['date','time']).reset_index()              # order by date, new index
            df = df.reindex(columns = new_columns)                          # adds & removes columns to create uniform output
         
            df.to_csv(account_name + ".csv")                                # write to file
    os.chdir('..')
    os.chdir('..')
    

if __name__ == "__main__":
    reformat()
