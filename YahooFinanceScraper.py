import requests
import ujson
import configparser


def parse_data(key, data):
    if key in data and data[key] is not None:
        return data[key]

    return None


class YahooFinanceScraper:

    def __init__(self, path):
        self.__url = "https://finance.yahoo.com/quote/"
        self.config = configparser.ConfigParser()
        self.config.read(path)

    def get_default_data(self, stock, section):
        ticker = stock.get_parameter['ticker']
        print(ticker)
        html = requests.get(url=self.__url + ticker + self.config[section]['url'], proxies=None)
        stock = None

        if html.status_code == requests.codes.ok:
            json_string = html.text.split('root.App.main =')[1].split('(this)')[0].split(';\n}')[0].strip()

            if 'QuoteSummaryStore' in json_string:
                json = ujson.loads(json_string)['context']['dispatcher']['stores']['QuoteSummaryStore']
                clean_string = ujson.dumps(json).replace('{}', 'null')
                data = ujson.loads(clean_string)

                for parameter in self.config[section]:
                    if parameter == 'url':
                        continue

                    key = self.config[section][parameter]

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

    def get_data(self, stock):
        for section in self.config.sections():
            self.get_default_data(stock, section)


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
