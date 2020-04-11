from Algorithms.Algorithm import Algorithm


class BasicAlgorithm(Algorithm):

    def __init__(self):
        super().__init__()
        self.__pe_value = 20
        self.__pb_value = 2

    def process(self, stock_list):
        output = []

        for stock in stock_list:
            stock_out = []
            score = 0

            if 0 < stock.get_pe_ratio() < self.__pe_value:
                score += 1

            if 0 < stock.get_pb_ratio() < self.__pb_value:
                score += 1

            if stock.get_dividend() > 0:
                score += 1

                if stock.get_payout_ratio() < 0.6:
                    score += 1

            stock_out.append(stock.get_symbol())
            stock_out.append(stock.get_name().replace(',', ''))
            stock_out.append(stock.get_sector().replace(',', ''))
            stock_out.append(stock.get_industry().replace(',', ''))
            stock_out.append(str(stock.get_price()))
            stock_out.append(str(stock.get_revenue()))
            stock_out.append(str(stock.get_profit()))
            stock_out.append(str(stock.get_debt()))
            stock_out.append(str(stock.get_market_cap()))
            stock_out.append(str(stock.get_pe_ratio()))
            stock_out.append(str(stock.get_pb_ratio()))
            stock_out.append(str(stock.get_payout_ratio()))
            stock_out.append(str(stock.get_dividend()))
            stock_out.append(str(score))

            output.append(stock_out)

        output.sort(key=lambda s: int(s[13]), reverse=True)

        header = ['Symbol', 'Name', 'Sector', 'Industry', 'Price',
                  'Revenue', 'Profit', 'Debt', 'Market Cap',
                  'P/E Ratio', 'P/B Ratio', 'PayoutRatio',
                  'Dividend', 'Score']
        output.insert(0, header)

        return output
