import numpy as np
import pandas as pd

def premium_bonds(df: pd.DataFrame):
    df["category"] = "internal"

    change_cat(df, "interest", "description", "prize")
    df["amount"] = np.where(
        df["description"].str.contains("deposit|prize"),
        df["amount"],
        df["amount"] * (-1),
    )
    return df