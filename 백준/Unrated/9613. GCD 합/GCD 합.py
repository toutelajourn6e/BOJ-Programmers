def get_gcd(a, b):
    while b:
        r = a%b
        a = b
        b = r
    return a

t = int(input())
sum = 0

for _ in range(t):
    k = 2
    n = list(map(int, input().split()))
    for i in n[1:]:
        for j in n[k:]:
            sum += get_gcd(i,j)
        k += 1
    print(sum)
    sum, k = 0, 0
    
