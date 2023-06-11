def radix(num, radix):
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    nums.reverse()
    return ''.join(nums)

def solution(n):
    return int(radix(n, 3)[::-1], 3)