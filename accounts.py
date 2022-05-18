import numpy as np
import pandas as pd

f = open('./account_list.csv','r')
accounts = f.readlines()
f.close()

df = pd.read_csv('./account_list (copy).csv')

print(df)


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
    df["currency"] = "GBP"

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
    df["currency"] = "GBP"


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

