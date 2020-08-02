from Algorithms.Algorithm import Algorithm


class BasicAlgorithm(Algorithm):

    def __init__(self):
        needs = ['pe_ratio', 'pb_ratio', 'payout_ratio', 'current_ratio', 'quick_ratio', 'gross_margin',
                 'debt_to_equity', 'debt_ratio', 'net_margin', 'receivables_turnover', 'return_on_equity']
        super().__init__(needs)
        self.__pe_value = 20
        self.__pb_value = 2
        self.__current_ratio_min = 1.2
        self.__current_ratio_max = 2
        self.__quick_ratio = 1
        self.__gross_margin = 20
        self.__debt_equity = 50
        self.__debt_ratio = 15
        self.__net_margin = 20
        self.__receivables_turnover = 5
        self.__return_on_equity = 20

    def process(self, stock_list):
        output = []

        for stock in stock_list:
            print('BA: ' + stock.get_parameter('ticker'))

            if super().verify_needs(stock):
                stock_out = []
                score = 0

                if 0 < stock.get_parameter('pe_ratio') < self.__pe_value:
                    score += 1

                if 0 < stock.get_parameter('pb_ratio') < self.__pb_value:
                    score += 1

                if stock.get_parameter('dividend') is not None and stock.get_parameter('dividend') > 0:
                    score += 1

                    if 0 < stock.get_parameter('payout_ratio') < 0.6:
                        score += 1

                if self.__current_ratio_min < stock.get_parameter('current_ratio') < self.__current_ratio_max:
                    score += 1

                if self.__quick_ratio < stock.get_parameter('quick_ratio'):
                    score += 1

                if self.__gross_margin < stock.get_parameter('gross_margin'):
                    score += 1

                if 0 < stock.get_parameter('debt_to_equity') < self.__debt_equity:
                    score += 1

                if 0 < stock.get_parameter('debt_ratio') < self.__debt_ratio:
                    score += 1

                if self.__net_margin < stock.get_parameter('net_margin'):
                    score += 1

                if self.__receivables_turnover < stock.get_parameter('receivables_turnover'):
                    score += 1

                if self.__return_on_equity < stock.get_parameter('return_on_equity'):
                    score += 1

                stock_out.append(stock.get_parameter('ticker'))
                stock_out.append(stock.get_parameter('name').replace(',', ''))
                stock_out.append(str(score))
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

                stock_out.append(str(stock.get_parameter('current_ratio')))
                stock_out.append(str(stock.get_parameter('quick_ratio')))
                stock_out.append(str(stock.get_parameter('gross_margin')))
                stock_out.append(str(stock.get_parameter('operating_margin')))
                stock_out.append(str(stock.get_parameter('debt_to_equity')))
                stock_out.append(str(stock.get_parameter('debt_ratio')))
                stock_out.append(str(stock.get_parameter('net_margin')))
                stock_out.append(str(stock.get_parameter('receivables_turnover')))
                stock_out.append(str(stock.get_parameter('asset_turnover')))
                stock_out.append(str(stock.get_parameter('return_on_equity')))

                output.append(stock_out)

        output.sort(key=lambda s: int(s[2]), reverse=True)

        header = ['Symbol', 'Name', 'Score', 'Sector', 'Industry', 'Price', 'Revenue', 'Profit', 'Debt', 'Market Cap',
                  'P/E Ratio', 'P/B Ratio', 'Payout Ratio', 'Dividend', 'Current Ratio', 'Quick Ratio', 'Gross Margin',
                  'Operating Margin', 'Total Debt to Equity', 'Total Debt to Assets', 'Net Margin',
                  'Receivables Turnover', 'Total Asset Turnover', 'Return on Equity']
        output.insert(0, header)

        return output
