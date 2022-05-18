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
    os.chdir('./csv_data/cash')
    df = pd.read_csv('Starling.csv',)

    # drop duplicate dates, keeping last balance, dropping unnecessary columns
    df = df.drop_duplicates(subset=["date"], keep="last").reset_index()
    df = df.reindex(columns = ['date','currency','balance'])

    df["starling"] = df.apply(currency_panda, axis=1)
    df = df.drop(columns = ['currency','balance'])

    df.set_index('date', inplace=True)

    df.to_csv('starling_balance.csv')

if __name__ == '__main__':
    balances()
    pass