import numpy as np
import pandas as pd
import psycopg2 
from psycopg2 import Error
import psycopg2.extras as extras

def connect():
    try:
        connection = psycopg2.connect(user="****",
                              password="***",
                              host="****",  
                              port="5432",
                              database="****")
        
        cursor = connection.cursor()
        print('server', connection.get_dsn_parameters(), "\n")

        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print('connected to -', record, "\n")

        return connection

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return False


def create_table():
    command = (
    """
    CREATE TABLE air_force_one (
        id SERIAL PRIMARY KEY,
        seller VARCHAR(255) NOT NULL,
        date VARCHAR(255) NOT NULL,
        title TEXT NOT NULL,
        price VARCHAR(255) NOT NULL,
        product_link TEXT NOT NULL,
        img_src TEXT NOT NULL,
        UNIQUE (seller, title)
        )
        """
        )
    
    try: 
        connection = connect()
        cursor = connection.cursor()
        resp = cursor.execute(command)

        cursor.close()
        connection.commit()
        print('table created')

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    
    finally:
        if connection is not None:
            connection.close()

def insertDf(connection, df, table):
    tuple_list = [tuple(x) for x in df.to_numpy()]

    print('tuple')
    for _tuple in tuple_list[0:3]:
        print(_tuple)

    cols = ','.join(list(df.columns))

    print('cols')
    print(cols)

    query  = "INSERT INTO %s(%s) VALUES %%s" % (table, cols) # you can also use f-string
    query = insert = "INSERT INTO %s(%s) VALUES %%s on conflict(seller, title) do nothing" % (table, cols) 
    print(f'\n\nquery: {query}')

    cursor = connection.cursor()
    try:
        extras.execute_values(cursor, query, tuple_list) # psycopg2.extras.execute_values() to insert the dataframe rows
        connection.commit() #deliver the chanhge
        print('inserted')

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        cursor.close()
        return False
    
    finally:
        cursor.close()
        return True
        
def sql_to_df(connection, table):
    df = pd.read_sql("SELECT * FROM %s" % (table), connection)
    print(df)
    return False

if __name__ == '__main__':
    print('running main')
    connect()
    # create_table()


    # df = pd.DataFrame({
    #     'seller': ["A", "B"],
    #     'date': ["date 1", "date 2"],
    #     'title': ["title 1", "title 2"],
    #     'price': ["price 1", "price 2"],
    #     'product_link':["link 1", "link 2"],
    #     'img_src': ["src 1", "src 2"]
    # })

    # print(df, '\n\n')
    # insertDf(connect(), df, 'air_force_one')

    sql_to_df(connect(), 'air_force_one')
