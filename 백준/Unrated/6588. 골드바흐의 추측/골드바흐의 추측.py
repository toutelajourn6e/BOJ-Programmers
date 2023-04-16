import sys

def prime_list(n):
    seive = [True for i in range(n+1)]
    m = int(n**0.5)
    
    for i in range(2, m+1):
        if seive[i] == True:
            j = 2
            while i*j <= n:
                seive[i*j] = False
                j += 1
    return [i for i in range(2, n+1) if seive[i] == True]
    
p = prime_list(1000000)
search = set(p)

while 1:
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        break
    
    for i in p:
        if (num - i) in search:
            print(f"{num} = {i} + {num-i}")
            break
