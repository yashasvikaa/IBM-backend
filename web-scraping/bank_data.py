import pandas as pd
def main():
    URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
    tables = pd.read_html(URL)
    df0, df1 = tables[0], tables[1]
    print(df0)
    print("DONE")
    print(df1)

if __name__ == "__main__":
    main()
