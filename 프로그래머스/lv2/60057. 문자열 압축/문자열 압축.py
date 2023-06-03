def solution(s):
    result = []
    n = len(s)
    if n == 1:
        return 1
    
    for i in range(1, n+1):
        start = s[:i]
        count = 1
        concat = ''
        for j in range(i, n+i, i):
            if start == s[j:j+i]:
                count += 1
            else:
                if count != 1:
                    concat += str(count) + start
                else:
                    concat += start
                
                start = s[j:j+i]
                count = 1
                
        result.append(len(concat))  
    return min(result)
            