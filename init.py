import os
import pandas as pd
import numpy as np


def init():
    f = 'account_list.csv'
    if f not in os.listdir():
        f = open(f, 'w')
        f.write('account_name,asset_type\n')
        f.close
        print('add your accounts to account_list.csv and run this again')
        return
    df = pd.read_csv(f)
    
    os.mkdir(os.path.join(df['asset_type'],df['account_name']), exist_ok=True)


if __name__ == '__main__':
    init()