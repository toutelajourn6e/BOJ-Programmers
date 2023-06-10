def solution(arr, divisor):
    ans = sorted([i for i in arr if i % divisor == 0])
    return ans if len(ans) > 0 else [-1]