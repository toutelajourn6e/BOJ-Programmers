def is_prime(n):
    if n < 2:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
    return True

n = int(input())
num = map(int, input().split())
p = 0

for i in num:
    if is_prime(i):
        p += 1
print(p)
    