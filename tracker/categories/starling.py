import numpy as np
import pandas as pd

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