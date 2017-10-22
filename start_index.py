from bs4 import BeautifulSoup
from urllib.request import urlopen

import requests
import csv, ujson
import utils, custom, config

DEBUG = True

INDEX = "house"
TYPE_NAME = "house"

class Downloader:
    def __init__(self, index_url):
        self.index = index_url

    def start_download(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result_html = requests.get(self.index, headers=headers)
        soup = BeautifulSoup(result_html.content.decode('utf-8'), 'html.parser')
        download_url = "https://www.redfin.com" + soup.select("#download-and-save")[0].get('href')

        response = urlopen(download_url)
        return next(csv.DictReader(response, fieldnames=custom.HOUSE_FIELDS))


class Indexer:
    def __init__(self, h_list):
        self.h_list = h_list

    def start_indexing(self):
        for h_odict in self.h_list:
            h_odict["location"] = "%s,%s" % (h_odict["latitude"], h_odict["longitude"])
            del h_odict["latitude"]
            del h_odict["longitude"]
            h_odict["address"] = {
                "address": h_odict["title"],
                "city": h_odict["city"],
                "state": h_odict["state"],
                "zipcode": h_odict["zip"]
                }
            del h_odict["city"]
            del h_odict["state"]
            del h_odict["zip"]
            h_json = ujson.dumps(h_odict)
            response = requests.post("%s/%s/%s" % (config.ELASTICSEARCH_URL, INDEX, TYPE_NAME), h_json, headers=config.HEADERS)
            print(response.content)


class CSVUtils:
    def genObjects(self, csv_file):
        csv_h = open(csv_file, 'r')
        next(csv_h) # Remove the first line which is the csv header
        return csv.DictReader(csv_h, fieldnames=custom.HOUSE_FIELDS)


if __name__ == "__main__":
    house_list = None
    if DEBUG:
        csv_file = "test.csv"
        house_list = CSVUtils().genObjects(csv_file)
    else:
        default_index_url = "https://www.redfin.com/city/17420/CA/San-Jose/filter/property-type=house+condo+townhouse+multifamily,max-price=700k"
        downloader = Downloader(default_index_url)
        house_list = downloader.start_download()

    indexer = Indexer(house_list)
    indexer.start_indexing()
