n, k = map(int, input().split())

num = [i for i in range(2, n+1)]
l = list()
while num:
    f = num[0]
    for i in range(f, n+1,f):
        if i in num:
            l.append(i)
            num.remove(i)


print(l[k-1])
