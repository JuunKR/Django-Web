from titanic.views.controller import Controller
from titanic.views.test import Test
from titanic.templates.plot import Plot


if __name__ == '__main__':
 #c p 앞에 놓는 이유 노출되면 해킹될 위험이있다
    controller = Controller()
    while 1:
        menu = input('0.exit\n'
                     '1. visualization\n'
                     '2. modeling\n'
                     '3. machine learning\n'
                     '4. machine release')
        if menu == '0':
            break
        elif menu == '1':
            plot = Plot('train.csv')
            # plot.draw_survived_dead()
            plot.draw_pclass()
            plot.draw_sex()
            plot.draw_embarked()


        elif menu == '2':
            controller.modeling('train.csv', 'test.csv')


        elif menu == '3':
            pass
        elif menu == '4':
            pass
        else:
            print('Wrong Number')
            continue
