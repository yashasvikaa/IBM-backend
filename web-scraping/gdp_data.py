import numpy as np
import pandas as pd

def main():
    URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

    # Extract tables from web page using pandas, retain table 3 as required data frame
    tables = pd.read_html(URL)
    df = tables[3]
    print(df)

    # Replace the column headers with column numbers
    df.columns = range(df.shape[1])

    # Retain columns with index 0 and 2 (name of the country & value of the GDP quoted by IMF)
    df = df[[0,2]]

    # Retain the Rows with index 1 to 10, indicating the top ten economies of the world.
    df = df.iloc[1:11,:]

    # Assign column names 'Country' and 'GDP (Million USD)'
    df.columns = ['Country', 'GDP (Million USD)']

    # Change the datatype of 'GDP (Million USD) 'column to integer.
    df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

    # Convert the GDP value in Million USD to Billion USD
    df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000

    # Round the values to 2 decimal places
    df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)

    # Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
    df = df.rename(columns= {'GDP (Million USD)': 'GDP (Billion USD)'})

    # Load the DataFrame to the CSV file named "Largest_economies.csv"
    df.to_csv('./Largest_economies.csv')

    print(df)


if __name__ == "__main__":
    main()