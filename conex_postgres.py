import psycopg2 as db
import psycopg2 as db
from faker import Faker

conn_string=conn_string = "host='localhost' port='5433' dbname='dataengineering' user='postgres' password='Shaba5796'"
conn=db.connect(conn_string)
cur=conn.cursor()

"""
query = "insert into users (id,name,street,city,zip) values({},'{}','{}','{}','{}')".format(1,'Big Bird','Sesame Street','Fakeville','12345')
cur.mogrify(query)
query2 = "insert into users (id,name,street,city,zip) values(%s,%s,%s,%s,%s)"
data=(1,'Big Bird','Sesame Street','Fakeville','12345')
cur.mogrify(query2,data)
cur.execute(query2,data)
"""
fake=Faker()
data=[]
i=2

for r in range(1000):
    data.append((i,fake.name(),fake.street_address(),
                fake.city(),fake.zipcode()))
    i+=1

data_for_db=tuple(data)

query = "insert into users (id,name,street,city,zip) values(%s,%s,%s,%s,%s)"
print(cur.mogrify(query,data_for_db[1]))
cur.executemany(query,data_for_db)


conn.commit()