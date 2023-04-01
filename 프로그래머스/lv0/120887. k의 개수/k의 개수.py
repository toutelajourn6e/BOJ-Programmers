def solution(i, j, k):
    answer = list()
    
    for s in range(i, j + 1):
        if s > 9:
            s2 = ' '.join(str(s)).split()
            
            for n in s2:
                if str(k) == str(n):
                    answer.append(n)
        else:
            if str(k) == str(s):
                answer.append(s)
                    
    return len(answer)
        
        