from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import requests


class NaverStock(object):
    url = 'https://finance.naver.com/item/sise_day.nhn?code=&page=1'
    driver_path = 'C:\\Program Files\\Google\\Chrome\\chromedriver'
    code = '000660' \
           '.'
    date_ls = []
    price_ls = []
    url_ls = []
    dt = {}
    df = None

    def input_code(self):
        pass

    def set_url(self):
        self.url = f'https://finance.naver.com/item/sise_day.nhn?code={self.code}&page='

    # def search(self):
    #     driver = webdriver.Chrome(self.driver_path)
    #     driver.get(self.url)
    #     time.sleep(0.5)
    #     element = driver.find_element_by_id("stock_items")
    #     element.send_keys(self.code)
    #     element.submit()
    #     time.sleep(0.5)
    #     driver.find_element_by_class_name("tab2").click()
    #     soup = BeautifulSoup(driver.page_source, 'html.parser')
    #     all_td = soup.find_all('td', {'class': "on"})

    def search(self):
        for i in range(10):
            self.url_ls.append(self.url + str(i + 1))
        driver = webdriver.Chrome(self.driver_path)

        for i in range(0,9):
            driver.get(self.url_ls[i])
            time.sleep(0.5)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_td = soup.find_all('td', {'align': 'center'})
            all_num = soup.find_all('td', {'class': 'num'})
            [self.date_ls.append(i.find('span').text) for i in all_td]
            [self.price_ls.append(i.find('span').text) for i in all_num]

    def insert_dt(self):
        for i, j in enumerate(self.date_ls):
            self.dt[i+1] = [j, self.price_ls[i]]

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dt, 'index', columns= ['Date', 'Price'])

    def df_to_csv(self):
        path = './data/naver_stock.csv'
        self.df.to_csv(path, ',', 'Nan')

if __name__ == '__main__':
    naver = NaverStock()
    # naver.code = input('코드를 입력하시오\n: ') #005930
    naver.set_url()
    naver.search()
    naver.insert_dt()
    naver.dict_to_dataframe()
    naver.df_to_csv()