import psycopg2 as db
import pandas as pd


conn_string=conn_string = "host='localhost' port='5433' dbname='dataengineering' user='postgres' password='Shaba5796'"
conn=db.connect(conn_string)

df=pd.read_sql("select * from users", conn)

df.to_json(orient='records')

