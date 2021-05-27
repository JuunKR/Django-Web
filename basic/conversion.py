import pandas as pd

class Conversion(object):

    @staticmethod
    def create_tuple() -> ():
        return (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    @staticmethod
    def tuple_to_list(ts) -> []:
        return  list(ts)


    @staticmethod
    def int_to_float(ls) -> []:
        return list(map(int, ls))
        # return [float(i) for i in ls]

    @staticmethod
    def float_to_int(ls) -> []:
        return [int(i) for i in ls]


    @staticmethod
    def list_to_dictionary(ls) -> {}:
        return {str(j) : [i] for i, j in enumerate(ls)}


    @staticmethod
    def str_to_tutple() -> ():
        return tuple('hello')

    @staticmethod
    def tuple_to_list2(s) -> []:
        return list(s)

    @staticmethod
    def dictionary_to_dataframe(d):
        return pd.DataFrame(d)

    @staticmethod
    def main():
        c = Conversion()
        s = ""
        ls = []
        t = ()
        d = {}
        index_name = [1]

        while 1: # 전부 리턴구조로 하기.
            menu = input("0. exit 1. input 2. output ")
            if menu == "0":
                break

            # 1부터 10까지 요소를 가진 튜플을 생성하시오.
            elif menu == '1':
                 t = c.create_tuple()
                 print(t)

            # 1번튜플을 리스트로 전환
            elif menu == '2':
                ls = c.tuple_to_list(t)
                print(ls)

            # 2번 리스트를 실수 리스트로 바꾸시오
            elif menu == '3':
                ls = c.int_to_float(ls)
                print(ls)
                print(type(ls))
            # 3번  실수 리스트를 정수 리스트로 전환하시오
            elif menu == '4':
                ls = c.float_to_int(ls)
                print(ls)

            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의의 인데스인데 str로 전환하시오
            elif menu == '5':
                d = c.list_to_dictionary(ls)
                print(d)

            # 'hello'를 튜플로 전환하기
            elif menu == '6':
                s = c.str_to_tutple()
                print(s)
            # 6번 튜플을 리스트로 전환하시오.

            elif menu == '7':
                s = c.tuple_to_list2(s)
                print(s)

           # 5번의 딕셔너리를 데이터프레임으로
            elif menu == '8':
                print(c.dictionary_to_dataframe(d))
            else:
                print('Wrong Number')
                continue


Conversion.main()





