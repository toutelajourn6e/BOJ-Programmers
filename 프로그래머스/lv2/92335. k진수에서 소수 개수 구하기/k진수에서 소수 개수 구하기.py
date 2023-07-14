def radix(num, radix):
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(digit)
    return ''.join(map(str, nums[::-1]))

def is_prime(num, k):
    num = int(num)
    m = int(num ** (0.5))
    for i in range(2, m+1):
        if not num % i: return False
    return True

def solution(n, k):
    ans = 0
    changed_num = radix(n, k).split('0')
    for num in changed_num:
        if not num or num == '1': continue
        if is_prime(num, k): ans += 1
        
    return ans