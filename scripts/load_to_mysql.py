import os
from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv

#load environmental variables
load_dotenv()
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")

#create database
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}")
with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS books_db"))
    conn.commit()

#create the connection
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

#read the csv with the cleaned data
df = pd.read_csv(r'C:\Users\anast\Desktop\web scraping\project\data\processed\cleaned_data.csv')

#send to sql
df.to_sql(
    name = 'books',
    con = engine,
    if_exists='replace',
    index=False
)

print('loaded seccessfully')