def solution(s):
    nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for index, num in enumerate(nums):
        s = s.replace(num, str(index))
            
    return int(s)