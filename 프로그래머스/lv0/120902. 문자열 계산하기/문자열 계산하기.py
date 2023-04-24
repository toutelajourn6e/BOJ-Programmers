def solution(my_string):
    s = list(my_string.split())
    nums = [i for i in s[::2]]
    ariths = [i for i in s[1::2]]
    ans = int(nums[0])
    del nums[0]
    
    for num, arith in zip(nums, ariths):
        if arith == '+':
            ans += int(num)
        else:
            ans -= int(num)
            
    
    return ans
        
        