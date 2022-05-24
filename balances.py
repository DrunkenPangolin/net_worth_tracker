import os
import pandas as pd
import personal_data
from datetime import date
from currency_converter import CurrencyConverter

c = CurrencyConverter(fallback_on_missing_rate=True)


def currency_panda(row: pd.DataFrame) -> pd.DataFrame:
    """function converts pandas rows/columns to desired currency"""
    (y, m, d) = map(int, row["date"].split("-"))
    return round(
        c.convert(
            row["balance"], row["currency"], personal_data.currency, date(y, m, d)
        ),
        2,
    )


def balances():
    """strips csv file to only date and end of day balance"""
    
    # change directory and open file
    dir = "csv_data"
    for x in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, x)):

            try:
                df = pd.read_csv(os.path.join(dir, x + ".csv"))
                print(x + ".csv imported successfully")
            except FileNotFoundError:
                print(x + ".csv does not exist")
                continue
            except Exception as e:
                print(e)
                continue

            # drop duplicate dates, keeping last balance, dropping unnecessary columns
            df = df.drop_duplicates(subset=["date"], keep="last").reset_index()
            df = df.reindex(columns=["date", "currency", "balance"])

            df[x] = df.apply(currency_panda, axis=1)
            df = df.drop(columns=["currency", "balance"])
            df.set_index("date", inplace=True)

            df.to_csv(os.path.join("balances", x + "_balance.csv"))


def unify():
    """unify all balance sheet in folder"""
    dir = "balances"
    bal_df = []

    for x in os.listdir(dir):
        bal_df.append(pd.read_csv(os.path.join(dir, x)))

    for df in bal_df:
        df.set_index(["date"], inplace=True)

    df = pd.concat(bal_df, join="outer", axis=1)
    df.index = pd.DatetimeIndex(df.index)
    df = df.reindex(pd.date_range(df.index.min(), df.index.max()))
    df = df.fillna(method="ffill")
    df = df.reindex(pd.date_range(personal_data.start_date, df.index.max()))

    df.to_csv("total.csv")


if __name__ == "__main__":
    balances()
    unify()
