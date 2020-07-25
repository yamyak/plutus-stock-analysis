import requests
import ujson
import configparser

from StockData import StockData


def parse_data(key, data):
    if key in data and data[key] is not None:
        return data[key]

    return None


class WebScraper:

    def __init__(self, path):
        self.__url = "https://finance.yahoo.com/quote/"
        self.config = configparser.ConfigParser()
        self.config.read(path)

    def get_data(self, symbol):
        print(symbol)
        html = requests.get(url=self.__url + symbol + "/", proxies=None)
        stock = None

        if html.status_code == requests.codes.ok:
            json_string = html.text.split('root.App.main =')[1].split('(this)')[0].split(';\n}')[0].strip()

            if 'QuoteSummaryStore' in json_string:
                json = ujson.loads(json_string)['context']['dispatcher']['stores']['QuoteSummaryStore']
                clean_string = ujson.dumps(json).replace('{}', 'null')
                data = ujson.loads(clean_string)

                stock = StockData()
                stock.add_parameter('symbol', symbol)

                for parameter in self.config['PARAMETERS']:
                    key = self.config['PARAMETERS'][parameter]

                    found = True
                    subsection = data
                    for sub_key in key.split('.'):
                        subsection = parse_data(sub_key, subsection)
                        if subsection is None:
                            found = False
                            break

                    value = None
                    if found:
                        value = subsection

                    stock.add_parameter(parameter, value)

        return stock


if __name__ == "__main__":
    sym = "INTC"
    req = requests.get("https://finance.yahoo.com/quote/" + sym + "/", proxies=None)
    json_s = req.text.split('root.App.main =')[1].split('(this)')[0].split(';\n}')[0].strip()
    js = ujson.loads(json_s)['context']['dispatcher']['stores']['QuoteSummaryStore']
    test = ujson.dumps(js, indent=4)
    # clean_str = ujson.dumps(js).replace('{}', 'null')
    # stock_data = ujson.loads(clean_str)
    # financial = stock_data['financialData']

    wait = 1
