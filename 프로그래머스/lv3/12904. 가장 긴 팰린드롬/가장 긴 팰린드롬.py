def solution(s):
    ans = 0
    
    for i in range(len(s)):
        for j in range(len(s), -1, -1):
            string = s[i:j]
            if string == string[::-1]:
                ans = max(ans, len(string))
                
    return ans