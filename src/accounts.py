import numpy as np
import pandas as pd


def accounts():
    df = pd.read_csv("./account_list.csv")
    df.set_index("account_name", inplace=True)
    # df['account_name'] = df['account_name'].str.lower().str.replace(' ','_')
    # print(df)
    return df


# cumulative sum (for balances) in pandas dataframe
# df['Balance'] = np.where(df['Status'].eq('Deposit'),df['Amount'], df['Amount'] * -1)
# df['Balance'] = df['Balance'].cumsum()


def change_cat(
    df: pd.DataFrame, new_category: str, column: str, criteria: str
) -> pd.DataFrame:
    df["category"] = np.where(
        df[column].str.contains(criteria), new_category, df["category"]
    )


def chase(df: pd.DataFrame):
    df.columns = ["date", "description", "amount", "balance", "action"]
    accs = accounts()

    # df["currency"] = np.where(accs['account_name'] == inspect.currentframe().f_code.co_name,df
    return df


def paypal(df: pd.DataFrame):
    return df


def premium_bonds(df: pd.DataFrame):
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

    # changing categories
    change_cat(
        df,
        "investments",
        "name",
        """
        Vanguard|
        AJ Bell|
        Freetrade|
        212|
        Halifax Share Dealing
        """,
    )
    change_cat(
        df,
        "internal",
        "name",
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
        """,
    )
    change_cat(df, "interest", "description", "nterest")
    return df


if __name__ == "__main__":
    accounts()
