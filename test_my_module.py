from modules import get_names
import pandas as pd


if __name__ == "__main__":
    print("test is being run directly")

    # Vi tilføjer ['navne'] for at udvælge den kolonne
    dfs = pd.read_excel("./data/unisex_navne.xls", header=None, names=['navne'])['navne']
    print(dfs)
    name_list = list(dfs)
    print(name_list)

    for name in get_names.get_one_name_bad(name_list):
        print(name)


    print('-------------/n')

    csv_file = './data/unisex_navne.csv'
    single_name = get_names.get_one_name_good(csv_file)
    print(next(single_name))
    print(next(single_name))
    print(next(single_name))
    print(next(single_name))

else:
    print("test is being imported into another module")