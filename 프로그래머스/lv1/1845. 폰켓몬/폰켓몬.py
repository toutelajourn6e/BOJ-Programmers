def solution(nums):
    take = len(nums) // 2
    nums = set(nums)
    
    if len(nums) >= take:
        return take
    else: return len(nums)