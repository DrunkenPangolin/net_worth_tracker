import numpy as np
import pandas as pd

def vm_current(df: pd.DataFrame):
    df = df.sort_index(ascending=False).reset_index()
    print(df)