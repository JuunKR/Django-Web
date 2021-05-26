from bs4 import BeautifulSoup
import requests
class Melon(object):
    URL = 'https://www.melon.com/chart/index.htm'
    headers = {'User-Agent': 'Mozilla/5.0'}
    titles = ''
    artists = ''
    dic = {}
    # req_melon
    def req_melon(self):
        request = requests.get(self.URL, headers=self.headers).text
        return BeautifulSoup(request, 'lxml')


    # 곡명(title), 가수(artist) 순위별, 앨범(album) 순위별
    def get_chart_all(self):
        for i in range(len(self.titles)):
            title = self.titles[i].text.strip().split('\n')[0]
            print(title)
            # artist = self.artists[i].text.strip().split('\n')[0]

            # self.dic[title] = artist
            # print('{:3}위 {} - {}'.format(i + 1, artist, title))
    @staticmethod
    def main():
        m = Melon()

        soup = m.req_melon()

        m.titles = soup.select('div.rank01')

        m.artists = soup.select('div.rank02>span')

        m.get_chart_all()
        print(m.dic)
Melon.main()

