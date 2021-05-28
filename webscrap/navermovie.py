# 객체지향 좀더 공부하자 스태틱과 다이내믹 차이
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
class NaverMovie(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = '' #영화 제목만 뽑을거니까 ''
    driver_path = 'C:\\Program Files\\Google\\Chrome\\chromedriver' # 알수없는것은 기본값으로 우선 두기
    ranking = []
    dt = {}
    df = None # 인스턴스를ㄹ

    def scrap(self,class_name):

        driver = webdriver.Chrome(self.driver_path)         #로컬변수를 만드는 이유 여러번 쓰겠다는 뜻
        driver.get(self.url)           # 주소를 구글한테 줌 우리가 편집 x 프레임워크
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class':class_name})
        [self.ranking.append(i.find('a').text) for i in all_div]
        print(self.ranking)

    def insert_dict(self):
        for i,j in enumerate(self.ranking):
            self.dt[f'{i+1}위'] = j

        print(self.dt)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dt, 'index', columns=['Title'])
        print(self.df)

    def df_to_csv(self):
        path = './data/naver.csv'
        self.df.to_csv(path, ',', 'Nan')


if __name__ == '__main__':
    naver = NaverMovie()
    naver.class_name = 'tit3'
    naver.scrap(naver.class_name)
    naver.insert_dict()
    naver.dict_to_dataframe()
    naver.df_to_csv()




