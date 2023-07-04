def solution(str1, str2):
    ans = []
    for i, j in zip(str1, str2):
        ans.append(i)
        ans.append(j)
        
    return ''.join(ans)