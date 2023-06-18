from itertools import permutations

def is_prime(digit):
    if digit < 2:
        return False
    
    for i in range(2, int(digit**(0.5))+1):
        if not digit % i:
            return False
        
    return True
    
    
    
def solution(numbers):
    n = len(numbers)
    result = 0
    numbers = list(numbers)
    
    arr = []
    for i in range(1, len(numbers)+1):
        arr.append(list(permutations(numbers, i)))
    
    num = [int(''.join(k)) for j in arr for k in j]
    print(num)
    for i in set(num):
        if is_prime(i):
            result += 1
        
    return result
        