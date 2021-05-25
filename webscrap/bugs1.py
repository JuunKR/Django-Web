from bs4 import BeautifulSoup
import requests

class Bugs(object):
    url = "https://music.bugs.co.kr/chart/track/realtime/total?"
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text


    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print("------------------ 제목 ----------------------")
        ls = soup.find_all('p', {'class': self.class_name[1]})
        for i in ls:
            print(f'{i.find("a").text}')
        print("------------------ 가수 ----------------------")
        ls = soup.find_all('p', {'class': self.class_name[0]})
        for i in ls:
            print(f'{i.find("a").text}')

    @staticmethod
    def main():
        bugs = Bugs()
        while 1:
            menu = input("0.종료 1.인풋 2.아웃풋")
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url(input('원하는 시간대를 입력하시오: '))


            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("tittle")
                bugs.get_ranking()
Bugs.main()

