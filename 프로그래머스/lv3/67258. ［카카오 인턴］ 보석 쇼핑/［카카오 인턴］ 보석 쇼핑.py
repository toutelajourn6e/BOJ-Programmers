def solution(gems):
    kind = len(set(gems))
    n = len(gems)
    ans = [0, n-1]
    
    dic = {gems[0]:1}
    left, right = 0, 0
    
    while right < n:
        if len(dic) < kind:
            right += 1
            if right == n:
                break
            dic[gems[right]] = dic.get(gems[right], 0) + 1
        else:
            if (right - left) < (ans[1] - ans[0]):
                ans = [left, right]
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            left += 1
    ans[0] += 1
    ans[1] += 1
            
    return ans