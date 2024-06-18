import psycopg2 as db

conn_string=conn_string = "host='localhost' port='5433' dbname='dataengineering' user='postgres' password='Shaba5796'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "select * from users"
cur.execute(query)

#for record in cur:
#    print(record)

datafile = cur.fetchmany(5)
print(datafile)

dataone = cur.fetchone()
print(dataone)

datarow =  cur.rowcount
print(datarow)

rownumber = cur.rownumber
print(rownumber)




