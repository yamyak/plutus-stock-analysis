from HTMLParser import HTMLParser
from enum import Enum
import configparser
import requests


class MarketWatchScraper(HTMLParser):

    def __init__(self, path):
        super().__init__()
        self.__url = "https://www.marketwatch.com/investing/stock/"
        self.__config = configparser.ConfigParser()
        self.__config.read(path)
        self.__current_stock = None
        self.__search_terms = {}
        self.__current_tag = None

    def parse_page_data(self, ticker, section):
        print(ticker)
        html = requests.get(url=self.__url + ticker + self.__config[section]['url'], proxies=None)

        if html.status_code == requests.codes.ok:
            self.feed(html.text)

    def setup_section_map(self, section):
        self.__search_terms.clear()
        for parameter in self.__config[section]:
            value = self.__config[section][parameter]
            self.__search_terms[value] = parameter

    def get_data(self, stock):
        self.reset()

        self.__current_stock = stock
        for section in self.__config.sections():
            self.setup_section_map(section)
            self.parse_page_data(stock.get_parameter['ticker'], section)

    def handle_data(self, data):
        if self.__current_tag is not None:
            self.__current_stock.set_parameter(self.__curent_tag, data)
            self.__current_tag = None
        elif data in self.__search_terms:
            self.__current_tag = self.__search_terms[data]
