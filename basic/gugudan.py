'''
구구단 프로그램은 단을 입력받아서, 입력받은 단의 1~9의 곱을 출력하는 어플이다.
단은 단은 정수이다
'''

class Gugudan(object):

    dan = 0
    dict = {}

    def reuslt(self):
        print(f'-- {self.dan}단 --')
        for i in range(1,10):
            print(f'{self.dan} X {i} = {self.dan * i}')

    def all_dan(self):
        for i in range(2,10):
            print(f'-- {i}단 --')
            for j in range(1,10):
                print(f'{i} X {j} = {i * j}')


    def print_dict_all_dan(self):
        d = self.dict
        for i in range(1,10):
            d[i] = self.dan * i
        print('딕셔너리 출력')
        print(d)
        for k in d.keys():
            print(f'{self.dan} X {k} = {d.get(k)}')



    @staticmethod
    def main():
        gugudan = Gugudan()
        while 1:
            menu = input('\n0.exit 1.input dan: 2.all dan 3.input dan with dict')
            if menu == '0':
                break

            elif menu == '1':
                gugudan.dan = int(input('단: '))
                gugudan.reuslt()

            elif menu == '2':
                gugudan.all_dan()

            elif menu == '3':
                gugudan.dan = int(input('단 입력'))
                gugudan.print_dict_all_dan()

            else:
                print('Wrong Number')
                continue

Gugudan.main()
