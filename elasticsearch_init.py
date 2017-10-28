import config
import requests
import ujson

from urllib.parse import urlencode

class ElasticInitializer:
    def __init__(self):
        self.host = "http://localhost:9200"

    '''
    Configure Elasticsearch Settings. For now, it only has one shard
    '''
    def create_index(self, index_name):
        payload = ujson.dumps({
            "settings": config.SETTINGS,
        })
        response = requests.put("%s/%s" % (self.host, index_name), headers=config.HEADERS, data=payload)
        print(response.status_code)
        print(response.content)


    def update_mapping(self, index_name, type_name):
        payload = ujson.dumps({
            "properties": config.HOUSE_MAPPINGS[type_name]["properties"]
        })
        response = requests.put("%s/%s/_mapping/%s" % (self.host, index_name, type_name), headers=config.HEADERS, data=payload)
        print(response.status_code)
        print(response.content)


    def exists(self, index_name, type_name, MLS):
        select = ["_id"]
        query = "%s:%s" % ("MLS", MLS)
        url_query = {
            "stored_fields": select,
            "q": query
        }
        import pdb; pdb.set_trace()
        response = requests.get("%s/%s/%s/_search?%s" % (self.host, index_name, type_name, urlencode(url_query)), headers=config.HEADERS)
        print (response.content)


    def update(self, h_info):
        pass


    def delete_index(self, index_name):
        response = requests.delete("%s/%s" % (self.host, index_name), headers=config.HEADERS)
        print(response.status_code)
        print(response.content)

if __name__=="__main__":
    ei = ElasticInitializer()
    ei.create_index("house")
    ei.update_mapping("house", "house")
