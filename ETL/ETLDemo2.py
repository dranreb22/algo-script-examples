import pandas as pd
import pyodbc
import pandas as db
import os
import configparser
import sys


def connectandextract():
    config = configparser.ConfigParser()

    try:
        config.read('config.ini')
    except Exception as e:
        print('issue reading config: ' + str(e))
        sys.exit()

    server = config['CONFIG']['server']
    database = config['CONFIG']['database']

    try:
        conn = pyodbc.connect(driver='{ODBC DRIVER 17 FOR SQL Server}', server=server, database=database,
                              Trusted_Connection='yes')
    except Exception as e:
        print('issue connecting to db: ' + str(e))
        sys.exit()

    try:
        cursor = conn.cursor()

        cursor.execute("Select * from sys.tables where name in ('[2017_Yellow_Taxi_Trip_Data]', 'Example')")
        tables = cursor.fetchall()
        print(tables)
        print('---')
        for table in tables:
            df = pd.read_sql_query(f'select * from {table[0]}', conn)
            print(df.head(10))
            print('---')
            load(df, table[0])
    except Exception as e:
        print("Error: " + str(e))


def load(df, table):
    try:
        # imagine a server name for another db here, only have mssql server on local machine
        conn = pyodbc.connect("...")
        df.to_sql("...")#("f'{table}', if_exists='replace', index=False)
    except Exception as e:
        print("got to load, stopping test" + str(e))
        sys.exit()


connectandextract()
