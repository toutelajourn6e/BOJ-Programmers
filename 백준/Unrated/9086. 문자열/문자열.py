t = int(input())

for i in range(t):
    a = input()
    if len(a) == 1:
        print(a+a)
    else:
        print(a[0]+a[-1])