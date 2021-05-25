from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMusic(object):

    url = ''


    def __str__(self):
        return self.url


    @staticmethod
    def get_rank(soup, index):
        print(f'------------------------------ {index} Ranking ----------------------------------')
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": index[0]})):
            count += 1
            print(f'{str(count)}위')
            print(f'{index[0]}: {i.find("a").text}')

        for i in soup.find_all(name='p', attrs=({"class": index[1]})):
            count += 1
            print(f'{str(count)}위')
            print(f'{index[1]}: {i.find("a").text}')


#https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input("0. 종료 1. Input URL 2. Get Ranking \n: ")

            if menu == '0':
                break

            elif menu == '1':
                bugs.url = input('Input URL: ')

            elif menu == '2':
                print(f'Input URL is {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml') # 두번째 인자 파서
                print(soup)
                bugs.get_rank(soup, "artist")

                bugs.get_rank(soup, "title")


            else:
                print('Wrong Number')
                continue

BugsMusic.main()

