ELASTICSEARCH_URL = "http://localhost:9200"

HEADERS = {
    "Content-Type": "application/json"
}

SETTINGS = {
    "number_of_shards": 1
}

HOUSE_MAPPINGS = {
    "house": {
        "properties": {
            "MLS": {
                "type": "text"
            },
            "title": {
                "type": "keyword"
            },
            "url": {
                "type": "text"
            },
            "price": {
                "type": "long"
            },
            "internal_size": {
                "type": "double"
            },
            "house_type": {
                "type": "keyword"
            },
            "bed": {
                "type": "double"
            },
            "bath": {
                "type": "double"
            },
            "HOA": {
                "type": "integer"
            },
            "address": {
                "properties": {
                    "state": {"type": "text"},
                    "city": {"type": "keyword"},
                    "zipcode": {"type": "integer"},
                    "address": {
                        "type": "text",
                        "fields": {
                            "analyzed": {
                                "type": "text"
                            }
                        }
                    }
                }
            },
            "year_built": {
                "type": "integer"
            },
            "status": {
                "type": "text"
            },
            "location": {
                "type": "geo_point"
            },
        }
    }
}
