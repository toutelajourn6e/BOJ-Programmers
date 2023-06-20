def is_prime(digit):
    m = int(digit**(0.5))
    
    for i in range(2, m+1):
        if digit % i == 0:
            return False
    return True

def solution(nums):
    n = len(nums)
    result = 0
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    result += 1
                    
    return result