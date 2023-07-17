def radix(num, radix):
    nums = []
    hex = ['A', 'B', 'C', 'D', 'E', 'F']
    while num:
        num, digit = divmod(num, radix)
        if digit >= 10:
            digit = hex[digit%10]
        nums.append(digit)
    return ''.join(map(str, nums[::-1]))

def solution(n, t, m, p):
    nums = []
    for i in range(50000):
        nums.append(radix(i, n))
    nums = ''.join(['0'] + nums)
    
    result = []
    for i in range(p-1, len(nums), m):
        result.append(nums[i])
        if len(result) == t:
            break
    
    return ''.join(result)
    
    
    