from elasticsearch import Elasticsearch
import pandas as pd
from pandas import json_normalize
#from pandas.io.json import json_normalize

es = Elasticsearch("http://localhost:9200")

es.info()


doc={"query":{"match_all":{}}}
res=es.search(index="users", size=10)
print(res['hits']['hits'])

for doc in res['hits']['hits']:
    print(doc['_source'])

df = json_normalize(res['hits']['hits'])
doc={"query":{"match":{"name":"Ronald Goodman"}}}
res=es.search(index="users", size=10)
print(res['hits']['hits'][0]['_source'])

res=es.search(index="users",q="name:Ronald Goodman",size=10)
print(res['hits']['hits'][0]['_source'])

# Get City Jamesberg - Returns Jamesberg and Lake Jamesberg
doc={"query":{"match":{"city":"Jamesberg"}}}
res=es.search(index="users", size=10)
print(res['hits']['hits'])

# Get Jamesberg and filter on zip so Lake Jamesberg is removed
doc={"query":{"bool":{"must":{"match":{"city":"Jamesberg"}},
"filter":{"term":{"zip":"63792"}}}}}
res=es.search(index="users", size=10)
print(res['hits']['hits'])