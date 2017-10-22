import config
import requests
import ujson

class ElasticInitializer:
    def __init__(self):
        self.host = "http://localhost:9200"

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

    def update_mapping(self):
        headers = {
            "Content-Type": "application/json"
        }
        payload = ujson.dumps({
            "mappings": config.HOUSE_MAPPINGS
        })
        index_name = "house"
        response = requests.put("%s/%s/_mapping/%s" % (self.host, index_name, "house"), headers=headers, data=payload)
        print(response.status_code)
        print(response.content)

if __name__=="__main__":
    ei = ElasticInitializer()
    #ei.create_index()
    ei.update_mapping()
