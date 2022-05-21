import os


def init():
    """creates appropriate files and folders for"""
    f = "account_list.csv"
    folders = ["csv_data", "balances", "expenses"]

    if f not in os.listdir():
        f = open(f, "w")
        f.write("account_name,asset_type,currency,csv_headings\n")
        f.close
        print("add your accounts to account_list.csv and run this again")
        return
    f = open(f, "r")

    for x in folders:
        os.makedirs(x, exist_ok=True)
    os.chdir(folders[0])

    accounts = []
    for i in f.readlines()[1:]:
        accounts.append(i.split(","))
    for j in accounts:
        if j[0] != "":
            os.makedirs(j[0], exist_ok=True)


if __name__ == "__main__":
    init()
