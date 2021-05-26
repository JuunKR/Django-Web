class Gugudan(object):
    dan = 0

    def clas(self):
        print(f'-- {self.dan} --')
        for i in range(1,10):
            print(f'{self.dan} X {i} = {self.dan * i}')




    @staticmethod
    def main():
        gugudan = Gugudan()
        while 1:
            menu = input('\n0.exit 1.단 입력 2.모든단 출력\n: ')
            if menu == '0':
                break
            elif menu == '1':
                gugudan.dan = int(input('단 : '))
                gugudan.clas()

            elif menu == '2':
                gugudan.full()

            else:
                print('Wrong Number')

Gugudan.main()
