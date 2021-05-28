class VectorTest(object):

    ls = ['abcd', 786, 2.23, 'john', 70.2]
    tinyls = [123, 'john']
    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')
    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'홍' : '30세'}

    def ls_create(self ):
        self.ls.append(100)
        print(self.ls)

    def ls_read(self):
        print(self.ls)

    def ls_update(self):
        print(self.ls + self.tinyls)


    def ls_delete(self):
        self.ls.remove(786)

    def tp_create(self):


    def tp_read(self):
        print(self.tp)
    def tp_update(self):
        print()

    def tp_delete(self):
        pass

    def dt_create(self):
        pass

    def dt_read(self):
        pass

    def dt_update(self):
        pass

    def dt_delete(self):
        pass



    @staticmethod
    def main():
        v = VectorTest()

        while 1:
            menu = input('List: 1.Create 2. Read 3.Update 4.Delete\n'
                         'Tuple: 5.Create 6. Read 7.Update 8.Delete\n'
                         'Dictionary: 9.Create 10. Read 11.Update 12.Delete\n: ')
            if menu == '1':
                v.ls_create()

            elif menu == '2':
                v.ls_read()

            elif menu == '3':
                v.ls_update()

            elif menu == '4':
                v.ls_delete()

            elif menu == '5':
                v.tp_create()

            elif menu == '6':
                v.tp_read()

            elif menu == '7':
                v.tp_update()

            elif menu == '8':
                v.tp_delete()

            elif menu == '9':
                v.dt_create()

            elif menu == '10':
                v.dt_read()

            elif menu == '11':
                v.dt_update()
            elif menu == '12':
                v.dt_delete()



