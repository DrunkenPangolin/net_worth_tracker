import numpy as np
import pandas as pd

def chase(df: pd.DataFrame):
    df.columns = ["date", "description", "amount", "balance", "action"]
    accs = accounts()

    # df["currency"] = np.where(accs['account_name'] == inspect.currentframe().f_code.co_name,df
    return df