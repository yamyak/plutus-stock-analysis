class StockData:

    def __init__(self, symbol):
        self.__symbol = symbol
        self.__valid = False
        self.__name = ""
        self.__sector = ""
        self.__industry = ""
        self.__revenue = 0
        self.__profit = 0
        self.__debt = 0
        self.__market_cap = 0
        self.__pe_ratio = 0
        self.__pb_ratio = 0
        self.__dividend = 0
        self.__payout_ratio = 0
        self.__price = 0

    def get_symbol(self):
        return self.__symbol

    def get_name(self):
        return self.__name

    def get_valid(self):
        return self.__valid

    def get_sector(self):
        return self.__sector

    def get_industry(self):
        return self.__industry

    def get_revenue(self):
        return self.__revenue

    def get_profit(self):
        return self.__profit

    def get_debt(self):
        return self.__debt

    def get_market_cap(self):
        return self.__market_cap

    def get_pe_ratio(self):
        return self.__pe_ratio

    def get_pb_ratio(self):
        return self.__pb_ratio

    def get_dividend(self):
        return self.__dividend

    def get_payout_ratio(self):
        return self.__payout_ratio

    def get_price(self):
        return self.__price

    def set_symbol(self, symbol):
        self.__symbol = symbol

    def set_name(self, name):
        self.__name = name

    def set_valid(self, valid):
        self.__valid = valid

    def set_sector(self, sector):
        self.__sector = sector

    def set_industry(self, industry):
        self.__industry = industry

    def set_revenue(self, revenue):
        self.__revenue = revenue

    def set_profit(self, profit):
        self.__profit = profit

    def set_debt(self, debt):
        self.__debt = debt

    def set_market_cap(self, market_cap):
        self.__market_cap = market_cap

    def set_pe_ratio(self, pe_ratio):
        self.__pe_ratio = pe_ratio

    def set_pb_ratio(self, pb_ratio):
        self.__pb_ratio = pb_ratio

    def set_dividend(self, dividend):
        self.__dividend = dividend

    def set_payout_ratio(self, payout_ratio):
        self.__payout_ratio = payout_ratio

    def set_price(self, price):
        self.__price = price
