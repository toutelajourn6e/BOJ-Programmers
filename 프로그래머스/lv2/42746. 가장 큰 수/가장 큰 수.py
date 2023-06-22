def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x * 4, reverse=True)
    result = ''.join(numbers)
    
    if int(result) == 0: return '0'
    else: return result

        
    
