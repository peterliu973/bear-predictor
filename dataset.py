import pandas as pd
import numpy as np
from sklearn import preprocessing

def read_csv(filename, ticker):
    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    df = df.rename(columns={'Close' : ticker})
    df = df.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1)
    return df
    
def read_quarterly(xls, ticker):
    
    df = xls.parse(ticker)
    df = df.rename(columns={'Qtr1' : 'Jan', 'Qtr2' : 'Apr', 'Qtr3' : 'Jul', 'Qtr4' : 'Oct'})    
    df = df.replace("\([P|R]\)*", "", regex=True)
      
    cols = df.columns[1:5]
        
    df = pd.melt(df, id_vars=['Year'], value_vars=cols)
    df['Date'] = pd.to_datetime(df['variable'] + ' 1, ' + df['Year'].astype(str))
    df = df.rename(columns={'value' : ticker})
    df = df.drop(['variable', 'Year'], axis=1)
    df = df.set_index('Date')    
    
    return df
    
def read_monthly(xls, ticker):
    
    df = xls.parse(ticker)
    df = df.replace("\([P|R]\)*", "", regex=True)
    
    cols = df.columns[1:13]
    
    df = pd.melt(df, id_vars=['Year'], value_vars=cols)
    df['Date'] = pd.to_datetime(df['variable'] + ' 1, ' + df['Year'].astype(str))
    df = df.rename(columns={'value' : ticker})
    df = df.drop(['variable', 'Year'], axis=1)
    df = df.set_index('Date')
    
    return df
    
def normalize(df, index_name='Date'):
    # normalize data
    x1 = df.values
    cols = df.columns
    idx = df.index
                        
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x1)
    df = pd.DataFrame(x_scaled)
    
    df.columns = cols
    df[index_name] = idx
    df = df.set_index(index_name)
    
    return df
    
    
    