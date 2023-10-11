import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('modified_unicorn_companies.csv')
    #print(df.head(10))
    #df.info()
    print(df.describe())
    #print(df.size)
    #print(df.shape)

    df['Date Joined'] = pd.to_datetime(df['Date Joined'])
    #df.info()

    df['Year Joined'] = df['Date Joined'].dt.year
    #print(df.head())

    df_sample = df.sample(n=50, random_state=42)

    df_sample['years_till_unicorn'] = df_sample['Year Joined'] - df_sample['Year Founded']

    grouped = df_sample[["Industry", "years_till_unicorn"]].groupby('Industry').max().sort_values(
        by="years_till_unicorn")
    #print(grouped)

    plt.bar(grouped.index, grouped["years_till_unicorn"])
    plt.title("Bar plot of maximum years taken by company to become unicorn per industry (from sample)")
    plt.xlabel("Industry")
    plt.ylabel("Maximum number of years")
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.subplots_adjust(bottom=0.45)
    #plt.show()


main()
