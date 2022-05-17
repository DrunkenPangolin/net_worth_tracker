import pandas as pd
import numpy as np
import os
from currency_converter import CurrencyConverter
c = CurrencyConverter(fallback_on_missing_rate=True)
from datetime import date

desired_currency = 'GBP'

def currency_panda(row):
    return round(c.convert(row['balance'],row['currency'],desired_currency, date(int('2019-05-01'.split('-')[0]),int('2019-05-01'.split('-')[1]),int('2019-05-01'.split('-')[2]))),2)

def balances():
    # change directory and open file
    os.chdir('./csv_data/cash')
    df = pd.read_csv('Starling.csv')

    # drop duplicate dates, keeping last balance, dropping unnecessary columns
    df = df.drop_duplicates(subset=["date"], keep="last").reset_index()
    df = df.reindex(columns = ['date','currency','balance'])

    df["starling"] = df.apply(currency_panda, axis=1)
    df = df.drop(columns = ['currency','balance'])

    df.to_csv('starling_balance.csv')

if __name__ == '__main__':
    balances()
    pass