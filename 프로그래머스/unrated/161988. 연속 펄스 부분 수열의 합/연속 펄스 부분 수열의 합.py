def solution(sequence):
    first = [0]
    second = [0]
    pos_start, neg_start = 1, -1
    
    for num in sequence:
        f_value = num * pos_start
        s_value = num * neg_start

        if first[-1] + f_value < f_value:
            first.append(f_value)
        else: first.append(first[-1] + f_value)
        
        if second[-1] + s_value < s_value:
            second.append(s_value)
        else: second.append(second[-1] + s_value)
        
        pos_start, neg_start = neg_start, pos_start
        
    return max(max(first), max(second))