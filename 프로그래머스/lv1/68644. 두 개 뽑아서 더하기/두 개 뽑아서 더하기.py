def solution(numbers):
    result = set()
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            sum_v = numbers[i] + numbers[j]
            result.add(sum_v)
            
                
    return sorted(result)