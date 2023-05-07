def solution(n):
    ans = 1
    for i in range(1, n):
        temp = i
        for j in range(i+1, n):
            temp += j
            if temp == n:
                ans += 1
                break
            elif temp < n:
                continue
            else:
                break
    return ans             