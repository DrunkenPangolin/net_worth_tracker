import os


def init():
    """creates appropriate files and folders for"""
    
    os.chdir("..")

    ACCOUNT_LIST = "account_list.csv"
    FOLDERS = ["csv_data", "balances", "expenses"]

    for x in FOLDERS:
        os.makedirs(x, exist_ok=True)

    if ACCOUNT_LIST not in os.listdir():
        f = open(ACCOUNT_LIST, "w")
        f.write("account_name,asset_type,currency,csv_headings\n")
        f.close
        print("add your accounts to account_list.csv and run this again")
        return
    f = open(ACCOUNT_LIST, "r")

    os.chdir(FOLDERS[0])
    accounts = []

    for i in f.readlines()[1:]:
        accounts.append(i.split(","))
    for j in accounts:
        if j[0] != "":
            os.makedirs(j[0], exist_ok=True)


if __name__ == "__main__":
    init()
