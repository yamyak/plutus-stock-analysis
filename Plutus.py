from YahooFinanceScraper import YahooFinanceScraper
from InputParser import InputParser
from Algorithms.BasicAlgorithm import BasicAlgorithm
from ExportCSV import ExportCSV
from StockData import StockData

import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    yfScraper = YahooFinanceScraper(config['YF_MAP']['path'])
    importer = InputParser(config['STOCK_LIST']['path'])

    portfolio = []
    for symbol in importer.get_stock_list():
        stock = StockData(symbol)
        yfScraper.get_data(stock)
        if stock is not None:
            portfolio.append(stock)

    algorithm = BasicAlgorithm()
    output = algorithm.process(portfolio)

    exporter = ExportCSV(config['OUTPUT']['path'])
    exporter.write(output)
