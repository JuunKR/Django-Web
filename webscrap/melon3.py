from bs4 import BeautifulSoup
import  requests

class Melon(object):
    ulr = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User - Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self):
        pass

    def get_ranking(self):
        pass

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('0.exit 1.')
