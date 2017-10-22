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
            "mappings": config.HOUSE_MAPPINGS
        })
        index_name = "house"
        response = requests.put("%s/%s" % (self.host, index_name), headers=headers, data=payload)
        print(response.status_code)
        print(response.content)


if __name__=="__main__":
    ei = ElasticInitializer()
    ei.create_index()
