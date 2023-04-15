m, n = map(int, input().split())

def prime_list(m, n):
    seive = [True]*(n+1)
    r = int((n+1)**0.5)
    
    for i in range(2, r+1):
        if seive[i] == True:
            for j in range(i+i,n+1,i):
                seive[j] = False
    return [i for i in range(m, n+1) if seive[i] == True]
 
num = prime_list(m, n)

for i in num:
    if i > 1:
        print(i)