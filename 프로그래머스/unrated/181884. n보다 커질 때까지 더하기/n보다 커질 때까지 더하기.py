def solution(numbers, n):
    ans = 0
    for i in numbers:
        ans += i
        if ans > n:
            return ans