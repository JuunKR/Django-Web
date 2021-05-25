class Member(object):

    id = ''
    pw = ''
    email = ''



    def join(self):
        pass

    def mypage(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass




    @staticmethod
    def main():

        member = Member()
        while 1:
            menu = input('0.종료 1.회원가입 2.로그인 3.내정보보기 4.수정 5.탈퇴')
            if menu == '0':
                break

            elif menu == '1':
                member.id = ''
                member.pw = ''
                member.email = ''

            elif menu == '2':
                pass

            elif menu == '3':
                member.__str__()

            elif menu == '4':
                pass
            elif menu == '5':
                pass
            else:
                continue


Member.main()