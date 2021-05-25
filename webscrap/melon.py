import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Melon(object):
    url = ''


    def __str__(self):
        return self.url


    @staticmethod
    def get_rank(soup, index):
        print(f'--------------------------Ranking----------------------------')
        count = 0
        for i in soup.find_all('div', attrs=({"class": index})):
            count += 1
            print(f'{str(count)}위')
            print(f'Artist: {i.find("a").text}')

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input("0. 종료, 1. URL입력 2. 랭킹확인 \n")
            if menu == "0":
                break

            elif menu == "1":
                melon.url = input("주소를 입력하시오: ")

            elif menu == "2":
                print(f'Input URL is {melon}')
                header01 = { 'User-Agent' : 'Mozilla/5.0'}
                modi01 = urllib.request.Request(melon.url, headers=header01 )
                soup = BeautifulSoup(urlopen(modi01), 'lxml')
                melon.get_rank(soup, "ellipsis rank02")

                melon.get_rank(soup, "ellipsis rank01")

            else:
                print("올바른 값을 입력하시오.")
                continue









Melon.main()

