import numpy as np
import pandas as pd
import tabula

pdf = '/home/sam/Coding/net_worth_tracker/nw_private/csv_data/Chase/Chase Open to 2022-05.pdf'

def chase(pdf):
    df = tabula.read_pdf(pdf)
    print(df)
    return df