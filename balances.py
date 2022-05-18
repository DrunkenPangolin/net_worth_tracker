import pandas as pd
import numpy as np
import os
from currency_converter import CurrencyConverter
c = CurrencyConverter(fallback_on_missing_rate=True)
from datetime import date
import personal_data


def currency_panda(row):
    (y,m,d) = map(int,row['date'].split('-'))
    return round(c.convert(row['balance'],row['currency'], personal_data.currency, date(y,m,d)),2)

def balances():
    # change directory and open file
    dir = os.path.join('csv_data','cash')
    for x in os.listdir(dir):
        print(x)
        if os.path.isdir(os.path.join(dir, x)):

            try:
                df = pd.read_csv(os.path.join(dir,x+ '.csv'))
            except FileNotFoundError:
                print(x+ '.csv does not exist')
                continue
            except Exception as e:
                print(e)
                continue

            # drop duplicate dates, keeping last balance, dropping unnecessary columns
            df = df.drop_duplicates(subset=["date"], keep="last").reset_index()
            df = df.reindex(columns = ['date','currency','balance'])

            df[x] = df.apply(currency_panda, axis=1)
            df = df.drop(columns = ['currency','balance'])

            df.set_index('date', inplace=True)

            df.to_csv(os.path.join('csv_data','balances',x + '_balance.csv'))

if __name__ == '__main__':
    balances()
