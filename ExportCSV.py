import csv


class ExportCSV:

    def __init__(self, path):
        self.__path = path

    def write(self, stock_data):
        with open(self.__path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(stock_data)
