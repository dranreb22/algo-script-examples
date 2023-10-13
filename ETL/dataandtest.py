import sys
import petl
import pyodbc
import configparser
import requests
import datetime
import json
import decimal
import pandas as pd
from scipy import stats


def main():
    # extracting and importing data
    df = pd.read_csv('waze_dataset.csv')

    # dictionary to map device type to numerical representation
    map_dictionary = {'Android': 2, 'iPhone': 1}

    # creating new column as an exact copy of older column
    df['device_type'] = df['device']

    # print(df.head())
    # remapping new column data to its numerical representation above
    df['device_type'] = df['device_type'].map(map_dictionary)

    # print(df.head())
    # group by device type to get the average drives/rides per device type
    print(df.groupby('device_type')['drives'].mean())

    # create a variable to hold just the iphone column and one to hold just the android column of drives
    # the internal df['device_type'] == 1] is grabbing all the data where the device type is one
    # then it only grabs the drives section from that data frame. same occurs for androids
    iPhone = df[df['device_type'] == 1]['drives']
    Android = df[df['device_type'] == 2]['drives']

    #running t-test (welchs t-test through scipy stats module, assuming not necessarily equal variance between the two
    #assumed sig of 5%, checking if p value is above.
    print(stats.ttest_ind(a=iPhone, b=Android, equal_var=False))


main()
