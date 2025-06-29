import pandas as pd
def main():
    URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
    tables = pd.read_html(URL)
    df0, df1 = tables[0], tables[1]
    print(df0, df1)
    print("DONE")
    df2 = tables[2]
    print(df2)
    
if __name__ == "__main__":
    main()
