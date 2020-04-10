class InputParser:

    def __init__(self, path):
        self.__stocks = []
        f = open(path, 'r')
        for line in f:
            self.__stocks.append(line.strip())

    def get_stock_list(self):
        return self.__stocks
