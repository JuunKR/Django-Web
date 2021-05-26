from bs4 import BeautifulSoup
import requests
class Bugs(object):
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    dict = {}
    def set_url(self,detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text
    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('--------- 제목 ---------')
        ls = soup.find_all('p',({"class": self.class_name[1]}))
        for i in ls:
            print(f'{i.find("a").text}')
        print('--------- 가수 ---------')
        ls = soup.find_all('p', ({"class": self.class_name[0]}))
        for i in ls:
            print(f'{i.find("a").text}')
    #키 제목
    def insert_title_dict(self): #  제목 뽑음
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all('p', ({"class": self.class_name[1]}))
        ls2 = soup.find_all('p', ({"class": self.class_name[0]}))
        for i in ls1:
            for j in ls2:
                self.dict[i.find("a").text] = j.find("a").text
        print('딕셔너리 출력')
        print(self.dict)
    @staticmethod
    def main():
        bugs = Bugs()
        while 1:
            menu = input('0.종료 1.입력 2.출력 3.')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url('20210526&charthour=13')
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.insert_title_dict()
            else:
                print('Wrong Number')
                continue
Bugs.main()