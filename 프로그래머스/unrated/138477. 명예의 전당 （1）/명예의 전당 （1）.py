def solution(k, score):
    result = []
    honor = []
    
    for index, v in enumerate(score):
        if index < k:
            honor.append(v)
            result.append(min(honor))
            continue
        honor.sort()
        if v > honor[0]:
            honor[0] = v
        result.append(min(honor))
        
            
    return result