def solution(k, ranges):
    col_num = [k]
    result = []
    
    while k != 1:
        if k % 2: 
            k = (k * 3) + 1
        else: 
            k //= 2
        col_num.append(k)
    
    for a, b in ranges:
        total = 0
        nums = col_num[a : len(col_num) + b]
        if a >= len(col_num) + b: 
            result.append(-1)
            continue
            
        for i in range(len(nums)-1):
            total += (nums[i] + nums[i+1]) / 2
        result.append(total)
        
    return result   