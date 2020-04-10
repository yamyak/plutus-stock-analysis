import requests
import ujson

from StockData import StockData


class WebScraper:

    def __init__(self):
        self.__url = "https://finance.yahoo.com/quote/"

    def get_data(self, name):
        html = requests.get(url=self.__url + name + "/", proxies=None)
        stock = StockData(name)

        if html.status_code == requests.codes.ok:
            json_string = html.text.split('root.App.main =')[1].split('(this)')[0].split(';\n}')[0].strip()

            if 'QuoteSummaryStore' in json_string:
                json = ujson.loads(json_string)['context']['dispatcher']['stores']['QuoteSummaryStore']
                clean_string = ujson.dumps(json).replace('{}', 'null')
                data = ujson.loads(clean_string)

                stock.set_valid(True)

                if 'financialData' in data:
                    fin_data = data['financialData']

                    if 'grossProfits' in fin_data and fin_data['grossProfits'] is not None:
                        stock.set_profit(fin_data['grossProfits']['raw'])

                    if 'totalRevenue' in fin_data and fin_data['totalRevenue'] is not None:
                        stock.set_revenue(fin_data['totalRevenue']['raw'])

                    if 'totalDebt' in fin_data and fin_data['totalDebt'] is not None:
                        stock.set_debt(fin_data['totalDebt']['raw'])

                    if 'currentPrice' in fin_data and fin_data['currentPrice'] is not None:
                        stock.set_price(fin_data['currentPrice']['raw'])

                if 'summaryProfile' in data:
                    profile = data['summaryProfile']

                    if 'industry' in profile and profile['industry'] is not None:
                        stock.set_industry(profile['industry'])

                    if 'sector' in profile and profile['sector'] is not None:
                        stock.set_sector(profile['sector'])

                if 'price' in data:
                    price = data['price']

                    if 'marketCap' in price and price['marketCap'] is not None:
                        stock.set_market_cap(price['marketCap']['raw'])

                if 'summaryDetail' in data:
                    detail = data['summaryDetail']

                    if 'trailingPE' in detail and detail['trailingPE'] is not None:
                        stock.set_pe_ratio(detail['trailingPE']['raw'])

                    if 'payoutRatio' in detail and detail['payoutRatio'] is not None:
                        stock.set_payout_ratio(detail['payoutRatio']['raw'])

                    if 'dividendRate' in detail and detail['dividendRate'] is not None:
                        stock.set_dividend(detail['dividendRate']['raw'])

                if 'defaultKeyStatistics' in data:
                    stats = data['defaultKeyStatistics']

                    if 'priceToBook' in stats and stats['priceToBook'] is not None:
                        stock.set_pb_ratio(stats['priceToBook']['raw'])

        return stock
