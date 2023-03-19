def solution(n):
    even_numbers = list()
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)
        
    return sum(even_numbers)
        