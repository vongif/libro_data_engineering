import elasticsearch
from elasticsearch import Elasticsearch
from faker import Faker
from elasticsearch import helpers



client = Elasticsearch("http://localhost:9200")

client.info()

fake=Faker()
"""doc={"name": fake.name(),"street": fake.street_address(),
"city": fake.city(),"zip":fake.zipcode()}
res=client.index(index="users", body=doc)
print(res['result']) #created 
"""

actions = [
    {
        "_index": "users",
        "_source": {
        "name": fake.name(),       
        "street": fake.street_address(),
        "city": fake.city(),
        "zip":fake.zipcode()
        }
    }
    for x in range(998) # or for i,r in df.iterrows()
]

res = helpers.bulk(client, actions)
print(res)

