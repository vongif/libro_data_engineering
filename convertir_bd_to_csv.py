import psycopg2 as db


conn_string=conn_string = "host='localhost' port='5433' dbname='dataengineering' user='postgres' password='Shaba5796'"
conn=db.connect(conn_string)
cur=conn.cursor()

f=open('fromdb.csv','w')

cur.copy_to(f,'users',sep=',')
f.close()

f=open('fromdb.csv','r')
f.read()


