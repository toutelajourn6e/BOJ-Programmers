def solution(n):
    divisor = list()
    
    for i in range(1, n + 1):
        if n % i == 0:
            divisor.append(i)
    
    return len(divisor)
            