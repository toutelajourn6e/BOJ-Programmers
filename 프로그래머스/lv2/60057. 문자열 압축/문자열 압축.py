def solution(s):
    n = len(s)
    if n == 1:
        return 1
    
    ans = 10000
    
    for i in range(1, n//2+1):
        temp = ''
        cnt = 1
        word = s[:i]
        
        for j in range(i, n, i):
            if s[j:j+i] == word:
                cnt += 1
        
            else:
                if cnt == 1:
                    temp += word
                else:
                    temp += str(cnt) + word
                word = s[j:j+i]
                cnt = 1
        if cnt == 1:
            temp += word
        else:
            temp += str(cnt) + word
        ans = min(ans ,len(temp))
        
    return ans
                
                
            
        
        