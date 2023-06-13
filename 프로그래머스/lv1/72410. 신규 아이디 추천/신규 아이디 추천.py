def solution(new_id):
    new_id = new_id.lower() # 1
    new_id = list(new_id)
    temp = []
    for char in new_id:
        if char.islower() or char.isdigit() or char in ['_', '-', '.']: # 2
            temp.append(char)
    
    del new_id
    result = []
    
    for char in temp:
        if result and char == '.' and result[-1] == '.': # 3
            continue
        else:
            result.append(char)
            
    del temp
    
    if result[0] == '.' and result[-1] == '.': # 4
        result = result[1:-1]
    elif result[0] == '.':
        result = result[1:]
    elif result[-1] == '.':
        result = result[:-1]
        
    if not len(result): # 5
        result.append('a')
    
    if len(result) > 15: # 6
        result = result[:15]
    if result[-1] == '.':
        result.pop()
        
    if len(result) < 3:
        while len(result) < 3:
            result.append(result[-1])
    
    return ''.join(result) 
    
    