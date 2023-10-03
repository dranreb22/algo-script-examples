import numpy as np
import pandas as pd


def main():
    df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv', nrows=100000)

    print(df.head())
    print('-----------------')
    df.info()
    print('-----------------')
    df.info(show_counts=True)
    print('-----------------')

    # df.describe()

    df_sort = df.sort_values(by=['trip_distance'], ascending=False)
    print(df_sort.head(10))

    df_sorted_total_amount = df.sort_values(by=['total_amount'], ascending=False)['total_amount']
    print(df_sorted_total_amount.head(10))
    print(df_sorted_total_amount.tail(10))

    print(df['payment_type'].value_counts())

    avg_cc_tip = df[df['payment_type'] == 1]['tip_amount'].mean()
    print('Avg. cc tip:', avg_cc_tip)

    avg_cash_tip = df[df['payment_type']==2]['tip_amount'].mean()
    print('Avg. cash tip:', avg_cash_tip)

    print(df['VendorID'].value_counts())

    print(df.groupby(['VendorID']).mean(numeric_only=True)[['total_amount']])

    card_pay = df[df['payment_type'] == 1]
    print(card_pay['passenger_count'].value_counts())

    print(card_pay.groupby(['passenger_count']).mean(numeric_only=True)[['tip_amount']])


main()
