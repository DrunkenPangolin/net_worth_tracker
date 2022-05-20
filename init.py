import os


def init():
    """creates appropriate files and folders for"""
    f = "account_list.csv"

    if f not in os.listdir():
        f = open(f, "w")
        f.write("account_name,asset_type,currency,csv_headings\n")
        f.close
        print("add your accounts to account_list.csv and run this again")
        return
    f = open(f, "r")

    folders = ['csv_data', 'balances', 'expenses']
    for x in folders:
        os.makedirs(x, exist_ok=True)
    os.chdir("csv_data")

    accounts = []
    for i in f.readlines()[1:]:
        accounts.append(i.split(","))
    for j in accounts:
        os.makedirs(os.path.join(j[1], j[0]), exist_ok=True)


if __name__ == "__main__":
    init()
