def solution(s):
    ans = len(s)
    
    for i in range(1, len(s)//2 + 1):
        start = s[:i]
        count = 1
        concat = ''
        for j in range(i, len(s), i):
            if start == s[j:j+i]:
                count += 1
            else:
                concat += str(count) + start if count > 1 else start
                start = s[j:j+i]
                count = 1
        
        concat += str(count) + start if count > 1 else start
        ans = min(ans, len(concat))
        
    return ans
        