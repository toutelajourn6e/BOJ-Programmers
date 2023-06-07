def solution(lines):
    line = [-1] * 201
    
    for i in lines:
        for j in range(i[0]+1, i[1]+1):
            line[j] += 1
    
    count = 0
    
    for k in line:
        if k > 0:
            count += 1
            
    return count
            