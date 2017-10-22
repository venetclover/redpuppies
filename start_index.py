from bs4 import BeautifulSoup

import requests
import csv

class Downloader:
    def __init__(self, index_url):
        self.index = index_url

    def start_download(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result_html = requests.get(self.index, headers=headers)
        soup = BeautifulSoup(result_html.content.decode(), 'html.parser')
        download_url = "https://www.redfin.com" + soup.select("#download-and-save")[0].get('href')

        house_list = None
        with requests.Session() as s:
            download = s.get(download_url)
            decoded_data = download.content.decode('utf-8')
            cr = csv.reader(decoded_data.splitlines(), delimiter=',')
            house_list = list(cr)

        return house_list

class Parser:
    def __init__(self, h_list):
        self.houses = h_list

    def gen_house_obj():
        pass


class Indexer:
    def __init__(self, h_list):
        self.h_list = h_list

    def start_indexing(self):
        pass


if __name__ == "__main__":
    default_index_url = "https://www.redfin.com/city/17420/CA/San-Jose/filter/property-type=house+condo+townhouse+multifamily,max-price=700k"
    downloader = Downloader(default_index_url)
    house_list = downloader.start_download()
    indexer = Indexer(house_list)
    indexer.start_indexing()
