def solution(s):
    s = s.split(" ")
    ans = [[] * len(s[0]) for _ in range(len(s))]
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j % 2 == 0:
                ans[i].append(s[i][j].upper())
            else:
                ans[i].append(s[i][j].lower())
                
    for k in range(len(ans)):
        ans[k] = ''.join(ans[k])
    
    return ' '.join(ans)
        