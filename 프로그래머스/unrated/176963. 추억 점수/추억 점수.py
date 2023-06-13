def solution(name, yearning, photos):
    result = []
    friends = {}
    
    for n, y in zip(name, yearning):
        friends[n] = y
    
    for photo in photos:
        sum_v = 0
        for i in photo:
            if i in friends:
                sum_v += friends[i]
        result.append(sum_v)
        
    return result