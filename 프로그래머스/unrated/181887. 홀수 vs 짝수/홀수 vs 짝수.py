def solution(num_list):
    even, odd = 0, 0
    
    for i in range(len(num_list)):
        if (i+1) % 2: odd += num_list[i]
        else: even += num_list[i]
    
    return max(even, odd)