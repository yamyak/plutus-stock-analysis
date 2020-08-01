from HTMLParser import HTMLParser
from enum import Enum


class MarketWatchPage(Enum):
    NONE = 0
    PROFILE = 1
    INCOME_STATEMENT = 2
    BALANCE_SHEET = 3
    CASH_FLOW = 4


class MarketWatchScraper(HTMLParser):

    def __init__(self):
        super().__init__()
        self.current_state = MarketWatchPage.NONE



    def handle_starttag(self, tag, attrs):
