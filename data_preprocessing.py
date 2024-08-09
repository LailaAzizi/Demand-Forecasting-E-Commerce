import pandas as pd
import sqlite3

def load_data(database_path):
    conn = sqlite3.connect(database_path)
    query = "SELECT * FROM sales_data;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def preprocess_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df
