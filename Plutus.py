from WebScraper import WebScraper
from InputParser import InputParser

import configparser


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    scraper = WebScraper()
    stocks = InputParser(config['INPUT']['path'])

    portfolio = []
    for stock_ticker in stocks.get_stock_list():
        stock = scraper.get_data(stock_ticker)
        if stock.get_valid():
            portfolio.append(stock)
