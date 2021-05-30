

a = 'https://finance.naver.com/item/sise_day.nhn?code={self.code}&page='
d = []

for i in range(10):
    d.append(a + str(i+1))
print(d)

