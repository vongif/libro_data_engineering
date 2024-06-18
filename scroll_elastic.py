from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
es.info()

res = es.search(
    index='users',
    scroll='20m',
    size='500',
    body={"query": {"match_all": {}}}
)

sid = res['_scroll_id']
size = res['hits']['total']['value']

while size > 0:
    res = es.scroll(scroll_id=sid, scroll='20m')
    sid = res['_scroll_id']
    size = len(res['hits']['hits'])
    for doc in res['hits']['hits']:
        print(doc['_source'])

