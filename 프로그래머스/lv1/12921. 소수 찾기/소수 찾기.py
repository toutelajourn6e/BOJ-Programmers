def get_primes(num):
    seive = [True] * (num+1)
    m = int(num**(0.5)) + 1
    
    for i in range(2, m):
        for j in range(i+i, num+1, i):
            if seive[j]:
                seive[j] = False
                
    return [i for i in range(2, num+1) if seive[i]]
    
    

def solution(n):
    return len(get_primes(n))