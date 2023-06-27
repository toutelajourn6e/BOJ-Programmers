def solution(dartResult):
    n = len(dartResult)
    ans = []
    score, i = 0, 0
    
    while True:
        if dartResult[i:i+2].isdigit():
            score = int(dartResult[i:i+2])
            i += 2
        else:
            score = int(dartResult[i])
            i += 1
        
        
        if dartResult[i] == 'S':
            i += 1
        elif dartResult[i] == 'D':
            score = score ** 2
            i += 1
        elif dartResult[i] == 'T': 
            score = score ** 3
            i += 1
            
        if i == n:
            ans.append(score)
            break
            
        if dartResult[i] == '*':
            if ans:
                ans[-1] *= 2
            score *= 2
            i += 1
        elif dartResult[i] == '#':
            score *= -1
            i += 1
        
            
        ans.append(score)
        score = 0
        
        if i == n:
            break
        
    return sum(ans)
        
        
            
        
    