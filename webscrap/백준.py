s1 = set('Hlelo') #[h], [e]
s2 = set( [3,1,2,3]  )
l1 = list(s1)


print(s1)
print(s2)

# {[h], [e]}
#
#
#
# { [1, 2, 3]}

def d(n):
    x = 0
    a = list(str(n))
    for i in a:
        x = x+int(i)
    return n+x

s_set = set()
for k in range(1,10000):
    s_set.add(d(k))
ans = set(range(1,10000)) - s_set
for num in sorted(ans):
    print(num)


lst = []
for i in range(1, 10000 + 1):
    lst.append(i)
for i in range(1, 10000 + 1):
    val = i
    sval = str(val)

    for j in sval:
        val += int(j)


    if lst.count(val) > 0:
        lst.remove(val)

for i in lst:
    print(i)