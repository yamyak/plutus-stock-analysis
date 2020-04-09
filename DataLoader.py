import requests
import ujson

from StockData import StockData


class DataLoader:

    def __init__(self):
        self.__url = "https://finance.yahoo.com/quote/"

    def get_data(self, name):
        html = requests.get(url=self.__url + name + "/", proxies=None).text
        json_string = html.split('root.App.main =')[1].split('(this)')[0].split(';\n}')[0].strip()
        json = ujson.loads(json_string)['context']['dispatcher']['stores']['QuoteSummaryStore']
        clean_string = ujson.dumps(json).replace('{}', 'null')
        data = ujson.loads(clean_string)

        stock = StockData(name)

        if data['financialData']['grossProfits'] is not None:
            stock.set_profit(data['financialData']['grossProfits']['raw'])

        if data['financialData']['totalRevenue'] is not None:
            stock.set_revenue(data['financialData']['totalRevenue']['raw'])

        if data['financialData']['totalDebt'] is not None:
            stock.set_debt(data['financialData']['totalDebt']['raw'])

        if data['financialData']['currentPrice'] is not None:
            stock.set_price(data['financialData']['currentPrice']['raw'])

        if data['summaryProfile']['industry'] is not None:
            stock.set_industry(data['summaryProfile']['industry'])

        if data['summaryProfile']['sector'] is not None:
            stock.set_sector(data['summaryProfile']['sector'])

        if data['price']['marketCap'] is not None:
            stock.set_market_cap(data['price']['marketCap']['raw'])

        if data['summaryDetail']['trailingPE'] is not None:
            stock.set_pe_ratio(data['summaryDetail']['trailingPE']['raw'])

        if data['summaryDetail']['payoutRatio'] is not None:
            stock.set_payout_ratio(data['summaryDetail']['payoutRatio']['raw'])

        if data['summaryDetail']['dividendRate'] is not None:
            stock.set_dividend(data['summaryDetail']['dividendRate']['raw'])

        if data['defaultKeyStatistics']['priceToBook'] is not None:
            stock.set_pb_ratio(data['defaultKeyStatistics']['priceToBook']['raw'])

        return stock
