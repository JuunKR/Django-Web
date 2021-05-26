from bs4 import BeautifulSoup
import  requests

class Melon(object):
    url = "https://www.melon.com/chart/index.htm?dayTime="
    headers = {'User-Agent': "Mozilla/5.0"}
    ls1 = []
    ls2 = []
    dic = {}

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all("div",{'class':"ellipsis rank02"})
        ls2 = soup.find_all("div", {'class': "ellipsis rank01"})
        for i in ls1:
            self.ls1.append({i.find("a").text})
            print(f'{i.find("a").text}')
        for i in ls2:
            self.ls2.append({i.find("a").text})
            print(f'{i.find("a").text}')

    def dict(self):
        # for i in range(0, len(self.ls2)):
        #     self.dic[i] = self.ls1[i]
        # print(self.dic)


        # 방법 2. zip
        for i, j in zip(self.ls1, self.ls2):
            self.dic[i] = j
        print(self.dic)

        '''
        for i, j in enumerate(self.ls2):
            self.dic[j] = self.ls1[i]

        print(self.dic)
        '''

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('0.종료 1.입력 2.랭킹 3.정리')
            if menu == '0':
                break
            elif menu == '1':
                melon.set_url('2021052618')


            elif menu == '2':
                melon.get_ranking()

            elif menu == '3':
                melon.dict()
            else:
                print('Wrong Number')
                continue
Melon.main()


