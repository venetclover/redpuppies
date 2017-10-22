import config
import requests
import ujson

class ElasticInitializer:
    def __init__(self):
        self.host = "http://localhost:9200"

    '''
    Configure Elasticsearch Settings. For now, it only has one shard
    '''
    def create_index(self):
        headers = {
            "Content-Type": "application/json"
        }
        payload = ujson.dumps({
            "settings": config.SETTINGS,
        })
        index_name = "house"
        response = requests.put("%s/%s" % (self.host, index_name), headers=headers, data=payload)
        print(response.status_code)
        print(response.content)

    def update_mapping(self, type_name):
        headers = {
            "Content-Type": "application/json"
        }
        payload = ujson.dumps({
            "properties": config.HOUSE_MAPPINGS[type_name]["properties"]
        })
        index_name = "house"
        response = requests.put("%s/%s/_mapping/%s" % (self.host, index_name, type_name), headers=headers, data=payload)
        print(response.status_code)
        print(response.content)

if __name__=="__main__":
    ei = ElasticInitializer()
    ei.create_index()
    ei.update_mapping("house")
