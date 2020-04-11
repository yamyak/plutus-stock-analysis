from WebScraper import WebScraper
from InputParser import InputParser
from Algorithms.BasicAlgorithm import BasicAlgorithm
from ExportCSV import ExportCSV

import configparser


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    scraper = WebScraper()
    importer = InputParser(config['INPUT']['path'])

    portfolio = []
    for symbol in importer.get_stock_list():
        stock = scraper.get_data(symbol)
        if stock.get_valid():
            portfolio.append(stock)

    algorithm = BasicAlgorithm()
    output = algorithm.process(portfolio)

    exporter = ExportCSV(config['OUTPUT']['path'])
    exporter.write(output)
