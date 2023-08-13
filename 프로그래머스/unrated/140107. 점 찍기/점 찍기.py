def solution(k, d):
    ans = 0
    nums = [i * k for i in range(d+1) if i * k <= d]

    for x in nums:
        y = int(((d ** 2) - (x ** 2)) ** 0.5)
        ans += (y // k) + 1
    
    return ans