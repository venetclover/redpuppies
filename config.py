SETTINGS = {
    "number_of_shards": 1
}

HOUSE_MAPPINGS = {
    "mappings": {
        "house": {
            "_all": {
                "enabled": True
            },
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
                "size": {
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
                "latitude": {
                    "type": "double"
                },
                "longitude": {
                    "type": "double"
                }
            }
        }
    }
}