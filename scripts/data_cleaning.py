import pandas as pd

df = pd.read_csv(r'C:\Users\anast\Desktop\web scraping\project\data\raw\dataset.csv')

print(f'Raw data from web Scrapping \n  {df.head()}')
print('\n \n \n')



#remove \n
df['Genre'] = df['Genre'].str.strip()

#remove Â£, type -> float
df['Price'] = df['Price'].str.replace('Â','', regex=False)
df['Price'] = df['Price'].str.replace('£','', regex=False).astype(float)

#remove ( from stock
df['Stock'] = df['Stock'].str.replace('(','',regex=False).astype(int)


print(f'Cleaned data \n  {df.head()}')
print('\n \n \n')

#checking the data types
print(df.dtypes)
print('\n \n \n')

#checking for null values
print(df.isnull().sum())

df.to_csv(r'C:\Users\anast\Desktop\web scraping\project\data\processed\cleaned_data.csv', index=False)

