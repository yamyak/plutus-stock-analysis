from StockData import StockData


class Algorithm:

    def __init__(self, needs):
        self.__weights = 0
        self.__needed_values = needs

    def verify_needs(self, stock):
        keys = stock.get_all_keys()
        for need in self.__needed_values:
            if need not in keys or stock.get_parameter(need) is None:
                return False

        return True

    def process(self, stock_list):
        return []
