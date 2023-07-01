def radix(num):
    nums = []
    while num:
        num, digit = divmod(num, 3)
        if digit == 0:
            num -= 1
            digit = 4
        nums.append(digit)
    return ''.join(map(str, nums[::-1]))
        
            

def solution(n):
    return radix(n)
        