from bs4 import BeautifulSoup
import requests

class Bugs(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    dict = {}
    title_ls = []
    artist_ls = []

    def set_url(self,detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all('p',({"class": self.class_name[1]}))
        ls2 = soup.find_all('p', ({"class": self.class_name[0]}))
        for i in ls1:
            self.title_ls.append(i.find("a").text)
            print(f'{i.find("a").text}')
        for i in ls2:
            self.artist_ls.append(i.find("a").text)
            print(f'{i.find("a").text}')


    #키 제목
    def insert_title_dict(self): #  제목 뽑음
        '''
        for i in self.title_ls:
            for j in self.artist_ls:
                self.dict[i] = j
        '''
        for i, j in enumerate(self.title_ls):
            self.dict[j] = self.artist_ls[i]
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
                print(bugs.set_url)


            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()

            elif menu == '3':
                bugs.insert_title_dict()

            else:
                print('Wrong Number')
                continue
Bugs.main()