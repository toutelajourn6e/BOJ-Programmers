def solution(s):
    ans = 0
    start = s[0]
    same = 1
    another = 0
    
    for i in range(1, len(s)):
        if s[i] == start:
            same += 1
        else:
            another += 1
        if same == another:
            ans += 1
            if i == len(s)-1:
                break
            start = s[i+1]
            same = 0
            another = 0
    else:
        ans += 1
        
    return ans