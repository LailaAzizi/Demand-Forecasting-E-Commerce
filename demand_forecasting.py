import pandas as pd
from fbprophet import Prophet
from data_preprocessing import load_data, preprocess_data

def forecast_demand(df):
    df = df.reset_index()
    df = df.rename(columns={'date': 'ds', 'sales': 'y'})
    
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    return forecast

if __name__ == "__main__":
    df = load_data('sales_data.db')
    df = preprocess_data(df)
    forecast = forecast_demand(df)
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
