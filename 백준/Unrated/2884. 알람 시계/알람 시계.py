a, b = map(int, input().split())

b += 15

if b >= 60:
    b -= 60
else:
    a -= 1
    if a < 0:
        a = 23

print(a ,b)