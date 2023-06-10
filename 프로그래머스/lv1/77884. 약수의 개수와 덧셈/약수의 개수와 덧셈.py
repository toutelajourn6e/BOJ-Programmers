def get_divisor(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt

def solution(left, right):
    ans = 0
    for i in range(left, right+1):
        cnt = get_divisor(i)
        if cnt % 2 == 0:
            ans += i
        else:
            ans -= i
        
    return ans