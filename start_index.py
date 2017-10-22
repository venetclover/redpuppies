from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import requests
import csv, ujson
import utils, custom, config

DEBUG = False

INDEX = "house"
TYPE_NAME = "house"

DEFAULT_INDEX_URL = "https://www.redfin.com/city/17420/CA/San-Jose/filter/property-type=house+condo+townhouse+multifamily,max-price=700k"
TEMP_FILENAME = "tmp.csv"

class Downloader:
    def __init__(self, index_url=DEFAULT_INDEX_URL):
        self.index = index_url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


    def start_download(self):
        if not DEBUG:
            self.download_list()

        return self.get_list()


    def download_fees(self, h_list):
        """
        Download fees from detail page
        h_list: OrderDict
        """
        for row in h_list:
            retrieve_details = {
                { "total": ("", "") },
                { "tax": ("", "") },
            }
            required_fields = self._get_fields(row["url"], retrieve_details)


    def download_list(self):
        """
        Download a list of house as csv file
        """
        required_fields = self._get_fields(self.index, {"download_url": ("#download-and-save", "href")})
        download_url = "https://www.redfin.com" + required_fields["download_url"][0]

        req_info = Request(download_url, None, self.headers)
        response = urlopen(req_info).read().decode('utf-8')
        wf = open(TEMP_FILENAME, 'w')
        wf.write(response)
        wf.close()


    def get_list(self):
        csv_file = "test.csv" if DEBUG else "tmp.csv"
        return CSVUtils().genObjects(csv_file)


    def _retreive(self, e, rtype):
        if rtype == "href":
            return e.get("href")
        elif rtype == "text":
            return e.text
        else:
            return e


    def _get_fields(self, url, required_fields):
        """
        This will extract the data by css selector.
        required_fields: Dict { key_that_return : (css_selector, type) }
        return: list of object ({ string: list })
        """
        result_html = requests.get(self.index, headers=self.headers)
        soup = BeautifulSoup(result_html.content.decode('utf-8'), 'html.parser')

        values = {}
        for k, (selector, rtype) in required_fields.items():
            values[k] = [self._retreive(e, rtype) for e in soup.select(selector)]
        return values


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
            break


class CSVUtils:
    def genObjects(self, csv_file):
        csv_h = open(csv_file, 'r')
        next(csv_h) # Remove the first line which is the csv header
        return csv.DictReader(csv_h, fieldnames=custom.HOUSE_FIELDS)


if __name__ == "__main__":
    house_list = Downloader().start_download()

    indexer = Indexer(house_list)
    indexer.start_indexing()
