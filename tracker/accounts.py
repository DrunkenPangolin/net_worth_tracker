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



if __name__ == "__main__":
    accounts()
