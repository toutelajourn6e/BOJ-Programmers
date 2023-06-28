def solution(n):
    result = 0
    
    while True:
        if n == 0:
            return result
        
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            result += 1