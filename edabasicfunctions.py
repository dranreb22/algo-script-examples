import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import time


def main():
    start_time = time.time()
    df = pd.read_csv('eda_using_basic_data_functions_in_python_dataset1.csv')
    df = df.head(10000)
    print(df.head())
    print(df.shape)
    df.info()

    df['date'] = pd.to_datetime(df['date'])
    print(df.head(10))
    print(df.groupby(['date']).sum().sort_values('number_of_strikes', ascending=False).head(10).reset_index())

    df['month'] = df['date'].dt.month
    print(df.head())

    newdf = df.drop('date', axis=1)
    print(newdf.head(12))
    print(newdf.groupby(['month']).sum().sort_values('number_of_strikes', ascending=False).head(12).reset_index())
    newdf['month_txt'] = df['date'].dt.month_name().str.slice(stop=3)
    df['month_txt'] = df['date'].dt.month_name().str.slice(stop=3)
    print(df.head())

    df_by_month = newdf.groupby(['month', 'month_txt']).sum().sort_values('month', ascending=True).head(
        12).reset_index()
    print(df_by_month)

    print(f'{time.time() - start_time:.2f}')

    plt.bar(x=df_by_month['month_txt'], height=df_by_month['number_of_strikes'], label="Number of strikes")
    plt.plot()

    plt.xlabel("Months(2018)")
    plt.ylabel("Number of lightning strikes")
    plt.title("Number of lightning strikes in 2018 by months")
    plt.legend()
    plt.show()

    print(f'{time.time() - start_time:.2f}')



main()
