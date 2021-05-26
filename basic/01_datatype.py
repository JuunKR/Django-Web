# *******************
#  --- Data Type ---
# *******************
#  ------ Atom ------
# *******************

'''
Python has Five standard types
Scalar
    Numbers : int, float, complex
    String :  str
Vector : List, Tuple, Dictionary, set
'''

# Scalar (Number, String)
# Scalar 가 모이면 Collection ------- Structure 의 유무
'''
hello = 'hello' # 변수는 메모리의 주소 값"
print(hello)
print(hello[1])
print(hello[2:5]) # String 은 list 라는 증명
'''

# ************* List CRUD Example *************

ls = ['abcd', 786, 2.23, 'join', 70.2] # ls = Atom 이랑 같은 차원?, Vector 급부터가 객체, 객체급 부터가 Atom, 기능을 부여하는 것은 Atom 부터, 객체는 내부적으로 메소드를 갖음 즉 기능
tinylist = [123, 'join']

# Reade : ls 의 목록을 출력
print(ls)

# Create : ls에 '100'을 추가
ls.append('100')
print(ls)
# print(ls)

# Update : ls와 tinylist 의 결합
ls = ls + tinylist
print(ls)

# Delete : ls 에서 786 을 제거
ls.remove(786)
print(ls)

# ************* Tuple CRUD Example *************
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')

# Create: tp 에 '100'을 추가 Create
print(tp + tuple('100'))
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
# Read: tp 의 목록을 출력
print(tp)

# Update: tp와 tinytp 의 결합
tp = tp + tinytp
print(tp)

# Delete: tp 에서 786을 제거
str = 'dkdkdk'
print(str)
vvv = [1,2,3]
print(vvv)
print(vvv[0])
print(str[0])
sss = 'hi'
vvv = 'python'
print(sss + vvv)
print(tuple(list[100]))



# ************* dictionary CRUD Example *************

dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'홍' : '30세'}

# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
dt['tom'] = 100
print(dt)

# Read: dt 의 목록을 출력
print(dt)

# Update: dt와 tinydt 의 결합
dt.update(tinydt)
print(dt)

# Delete: dt 에서 'abcd' 제거
del dt['abcd']
print(dt)


