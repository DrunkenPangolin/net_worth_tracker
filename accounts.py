import pandas as pd

f = open('./account_list.csv','r')
accounts = f.readlines()
f.close()

df = pd.read_csv('./account_list (copy).csv')

print(df)

class account:
    def __init__(self, name, asset_type) -> None:
        self.name = name
        self.asset = asset_type

#y = x.replace('\t',',')
for acc in accounts:
    if acc.strip() != '':
        y = acc.strip().split(',')
        # = account(y[0], y[1])


revolut = account('Revolut','Cash')
revolut.value = 0
#print(revolut.value)
    



#class cash(account):
#    self.asset = 'cash'

#class crypto(account):
#    self.asset = 'crypto'

