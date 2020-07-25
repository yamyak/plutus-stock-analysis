from Algorithms.Algorithm import Algorithm


class BasicAlgorithm(Algorithm):

    def __init__(self):
        needs = ['pe_ratio', 'pb_ratio', 'payout_ratio']
        super().__init__(needs)
        self.__pe_value = 20
        self.__pb_value = 2

    def process(self, stock_list):
        output = []

        for stock in stock_list:
            print(stock.get_parameter('symbol'))

            if super().verify_needs(stock):
                stock_out = []
                score = 0

                if 0 < stock.get_parameter('pe_ratio') < self.__pe_value:
                    score += 1

                if 0 < stock.get_parameter('pb_ratio') < self.__pb_value:
                    score += 1

                if stock.get_parameter('dividend') is not None and stock.get_parameter('dividend') > 0:
                    score += 1

                    if stock.get_parameter('payout_ratio') < 0.6:
                        score += 1

                stock_out.append(stock.get_parameter('symbol'))
                stock_out.append(stock.get_parameter('name').replace(',', ''))
                stock_out.append(stock.get_parameter('sector').replace(',', ''))
                stock_out.append(stock.get_parameter('industry').replace(',', ''))
                stock_out.append(str(stock.get_parameter('price')))
                stock_out.append(str(stock.get_parameter('revenue')))
                stock_out.append(str(stock.get_parameter('profit')))
                stock_out.append(str(stock.get_parameter('debt')))
                stock_out.append(str(stock.get_parameter('market_cap')))
                stock_out.append(str(stock.get_parameter('pe_ratio')))
                stock_out.append(str(stock.get_parameter('pb_ratio')))
                stock_out.append(str(stock.get_parameter('payout_ratio')))
                stock_out.append(str(stock.get_parameter('dividend')))
                stock_out.append(str(score))

                output.append(stock_out)

        output.sort(key=lambda s: int(s[13]), reverse=True)

        header = ['Symbol', 'Name', 'Sector', 'Industry', 'Price',
                  'Revenue', 'Profit', 'Debt', 'Market Cap',
                  'P/E Ratio', 'P/B Ratio', 'PayoutRatio',
                  'Dividend', 'Score']
        output.insert(0, header)

        return output
