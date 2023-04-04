t = int(input())

for i in range(t):
    a, b = input().split()
    a = int(a)
    c = ''
    for j in list(b):
        c += j*a
    print(c)
        