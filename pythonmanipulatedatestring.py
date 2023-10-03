import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    df = pd.read_csv('eda_manipulate_date_strings_with_python.csv')
    df = df.head(100000)
    print(df.head())

    df['date'] = pd.to_datetime(df['date'])
    df['week'] = df['date'].dt.strftime('%Y-W%V')
    df['month'] = df['date'].dt.strftime('%Y-%m')
    df['quarter'] = df['date'].dt.to_period('Q').dt.strftime('%Y-Q%q')
    df['year'] = df['date'].dt.strftime('%Y')
    print(df.head())

    newdf = df.drop('date', axis=1)
    df_by_week_2018 = newdf[newdf['year'] == '2018'].groupby(['week']).sum().reset_index()
    print(df_by_week_2018.head())

    plt.bar(x=df_by_week_2018['week'], height=df_by_week_2018['number_of_strikes'])
    plt.plot()
    plt.xlabel("Week number")
    plt.ylabel("Number of lightning strikes")
    plt.title("Number of lightning strikes per week (2018)")
    plt.show()

main()