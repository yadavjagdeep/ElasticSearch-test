from elasticsearch import Elasticsearch

class BaseElasticSearch:
    def __init__(self, host):
        self._host = host
        self._es = Elasticsearch(self._host, timeout=25)

    