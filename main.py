import csv
from faker import Faker
import csv
import pandas as pd



output=open('data.CSV','w')
fake=Faker()
header=['name','age','street','city','state','zip','lng','lat']
mywriter=csv.writer(output)
mywriter.writerow(header)
for r in range(1000):
    mywriter.writerow([fake.name(),fake.random_int(min=18,
    max=80, step=1), fake.street_address(), fake.city(),fake.
    state(),fake.zipcode(),fake.longitude(),fake.latitude()])
    
#output.close()

with open('data.csv') as f:

    myreader=csv.DictReader(f)
    headers=next(myreader)
    for row in myreader:
        print(row['name'])

df=pd.read_csv('data.CSV')
df.head(10)

print(df)

data={'Name':['Paul','Bob','Susan','Yolanda'],
'Age':[23,45,18,21]}

df=pd.DataFrame(data)

df.to_csv('fromdf.CSV',index=False)


