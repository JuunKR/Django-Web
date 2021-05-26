dan = 0
dict = []
d=dict

dan = input("입력")

for i in range(1,10):
    d[i] = dan * i
print('딕셔너리 출력')
print(d)
for k in d.keys():
    print(f'{dan} X {k} = {d.get(k)}')
