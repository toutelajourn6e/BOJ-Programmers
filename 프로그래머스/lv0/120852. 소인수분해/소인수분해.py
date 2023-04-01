def solution(n):
    answer = list()
    divisor = 2
    
    while divisor <= n:
        if n % divisor == 0:
            answer.append(divisor)
            n //= divisor
        else:
            divisor += 1
    
    return list(dict.fromkeys(answer))
        