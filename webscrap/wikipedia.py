class Wikipedia(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    @staticmethod
    def main():

        while 1:
            menu = input("--------------------------------------------\n"
                         "0. 종료 1. URL입력 2.URL출력\n: ")
            if menu == "0":
                break

            elif menu == '1':
                url = Wikipedia(input("URL을 입력하시오:  "))

            elif menu == '2':
                print(f'입력한 주소는 {url}입니다.')

            else:
                print('Wrong Number')
                continue
Wikipedia.main()
