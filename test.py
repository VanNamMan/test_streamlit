import pandas as pd
import numpy as np

DATA_URL = r"C:\Users\Unknown\Downloads\uber-raw-data-sep14.csv"
DATE_COLUMN = 'date/time'

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data = load_data(100)
# x = data[DATE_COLUMN].dt.hour
# print(type(x),x)

x = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))

print(type(x),x)