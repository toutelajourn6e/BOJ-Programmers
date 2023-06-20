def solution(s):
    result = []
    record = {}
    
    for index, char in enumerate(s):
        if not char in record:
            record[char] = index
            result.append(-1)
        else:
            result.append(index - record[char])
            record[char] = index
    
    return result
        