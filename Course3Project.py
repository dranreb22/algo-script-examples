import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    df = pd.read_csv("Course3_2017_Yellow_Taxi_Trip_Data.csv")
    print(df.head())
    print("----------")
    print(df.size)
    print("----------")
    print(df.describe())
    print("----------")
    df.info()
    print("----------")

    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    df.info()

    plt.figure(figsize=(7, 2))
    plt.title('Trip Distance')
    sns.boxplot(data=None, x=df['trip_distance'], fliersize=1)

    # plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(df['trip_distance'], bins=range(0, 35, 1))
    plt.title('Trip distance histogram')

    # plt.show()

    plt.figure(figsize=(7, 2))
    plt.title('Total Amount')
    sns.boxplot(data=None, x=df['total_amount'], fliersize=1)

    # plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(df['total_amount'], bins=range(0, 110, 5))
    plt.title('Total Amount histogram')

    # plt.show()

    plt.figure(figsize=(7, 2))
    plt.title('Tip Amount')
    sns.boxplot(data=None, x=df['tip_amount'], fliersize=1)

    # plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(df['tip_amount'], bins=range(0, 110, 5))
    plt.title('Tip Amount histogram')

    # plt.show()

    plt.figure(figsize=(7, 2))
    plt.title('Tip Amount')
    sns.boxplot(data=None, x=df['tip_amount'], fliersize=1)

    # plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(df['tip_amount'], bins=range(0, 110, 5))
    plt.title('Tip Amount histogram')

    # plt.show()

    plt.figure(figsize=(12, 7))
    ax = sns.histplot(data=df, x='tip_amount', bins=range(0, 21, 1),
                      hue='VendorID',
                      multiple='stack',
                      palette='pastel')
    ax.set_xticks(range(0, 21, 1))
    ax.set_xticklabels(range(0, 21, 1))
    plt.title('Tip amount by vendor histogram');

    # plt.show()

    plt.figure(figsize=(12, 7))
    ax = sns.histplot(data=df, x='tip_amount', bins=range(10, 21, 1),
                      hue='VendorID',
                      multiple='stack',
                      palette='pastel')
    ax.set_xticks(range(10, 21, 1))
    ax.set_xticklabels(range(10, 21, 1))
    plt.title('Tip amount by vendor histogram');

    # plt.show()

    df['passenger_count'].value_counts()

    mean_tips_by_passenger_count = df.groupby(['passenger_count']).mean(numeric_only=True)[['tip_amount']]
    # print(mean_tips_by_passenger_count)

    data = mean_tips_by_passenger_count.tail(-1)
    pal = sns.color_palette("Greens_d", len(data))
    rank = data['tip_amount'].argsort().argsort()
    plt.figure(figsize=(12, 7))
    ax = sns.barplot(x=data.index,
                     y=data['tip_amount'],
                     palette=np.array(pal[::-1])[rank])
    ax.axhline(df['tip_amount'].mean(), ls='--', color='red', label='global mean')
    ax.legend()
    plt.title('Mean tip amount by passenger count', fontsize=16);
    # print(mean_tips_by_passenger_count.head())
    # plt.show()

    df['month'] = df['tpep_pickup_datetime'].dt.month_name()
    df['day'] = df['tpep_pickup_datetime'].dt.day_name()
    monthly_rides = df['month'].value_counts()
    print(monthly_rides)
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                   'August', 'September', 'October', 'November', 'December']
    monthly_rides = monthly_rides.reindex(index=month_order)
    print(monthly_rides)

    plt.figure(figsize=(12, 7))
    ax = sns.barplot(x=monthly_rides.index, y=monthly_rides)
    ax.set_xticklabels(month_order)
    plt.title('Ride count by month', fontsize=16);

    # plt.show()

    daily_rides = df['day'].value_counts()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    daily_rides = daily_rides.reindex(index=day_order)
    print(daily_rides)

    test = np.round(np.random.normal(10, 5, (3000, 2)), 1)
    midway = int(len(test) / 2)
    start = test[:midway]
    end = test[midway:]

    distances = (start - end) ** 2
    distances = distances.sum(axis=-1)
    distances = np.sqrt(distances)

    test_df = pd.DataFrame({'start': [tuple(x) for x in start.tolist()],
                            'end': [tuple(x) for x in end.tolist()],
                            'distance': distances})
    data = test_df[['end', 'distance']].groupby('end').mean()
    data = data.sort_values(by='distance')

    plt.figure(figsize=(14, 6))
    ax = sns.barplot(x=data.index,
                     y=data['distance'],
                     order=data.index)
    ax.set_xticklabels([])
    ax.set_xticks([])
    ax.set_xlabel('Endpoint')
    ax.set_ylabel('Mean distance to all other points')
    ax.set_title('Mean distance between points taken randomly from normal distribution');

    plt.show()






main()
