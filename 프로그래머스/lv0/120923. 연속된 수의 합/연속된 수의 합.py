def solution(num, total):
    m = total / num
    result = list()
    
    if m.is_integer():
        c = num // 2
        result.append(m)
        for i in range(1, c+1):
            result.append(m-i)
            result.append(m+i)
        return sorted(result)
    
    else:
        result.append(int(m+0.5))
        result.append(int(m-0.5))
        m = int(m)
        
        for i in range(2, (num//2)+1):
            result.append(m-i+1)
            result.append(m+i)
            
        return sorted(result)