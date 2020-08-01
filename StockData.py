class StockData:

    def __init__(self, ticker):
        self.__parameters = {'ticker': ticker}

    def set_parameter(self, key, value):
        self.__parameters[key] = value

    def get_parameter(self, key):
        if key in self.__parameters:
            return self.__parameters[key]

        return None

    def get_all_keys(self):
        return self.__parameters.keys()
