from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import requests


class NaverStock(object):
    url = 'https://finance.naver.com/sise/sise_market_sum.nhn?&amp;page=3&page='
    driver_path = 'C:\\Program Files\\Google\\Chrome\\chromedriver'

    name_ls = []
    code_ls = []
    url_ls = []
    dt = {}
    df = None

    # def input_code(self):
    #     pass

    # def set_url(self):
    #     self.url = f'https://finance.naver.com/sise/sise_market_sum.nhn?&amp;page=3&page='

    def search(self):
        for i in range(10):
            self.url_ls.append(self.url + str(i + 1))
        driver = webdriver.Chrome(self.driver_path)

        for i in range(0, 9):
            driver.get(self.url_ls[i])
            time.sleep(0.5)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_a = soup.find_all('a', {'class': 'tltle'})
            for i in all_a:
                self.name_ls.append(i.text)
                self.code_ls.append(i['href'].split('code=')[1])

            # [self.name_ls.append(i.text) for i in all_a]
            # [self.code_ls.append(i['href'].split('code=')[1]) for i in all_a]

    def insert_dt(self):
        for i, j in enumerate(self.name_ls):
            self.dt[i+1] = [j, self.code_ls[i]]

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dt, 'index', columns= ['Name', 'Code'])

    def df_to_csv(self):
        path = './data/naver_homework.csv'
        self.df.to_csv(path, ',', 'Nan')

if __name__ == '__main__':
    naver = NaverStock()
    # naver.code = input('코드를 입력하시오\n: ') #005930
    # naver.set_url()
    naver.search()
    naver.insert_dt()
    naver.dict_to_dataframe()
    naver.df_to_csv()