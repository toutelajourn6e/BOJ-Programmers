def radix(num, radix):
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return ''.join(nums)

def solution(n):
    return int(radix(n, 3), 3)