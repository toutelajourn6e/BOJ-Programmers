def solution(food):
    table = []
    
    for food_num, cnt in enumerate(food):
        if not food_num:
            continue
        for _ in range(cnt//2):
            table.append(food_num)
            
    reverse_table = list(reversed(table))
    table = table + [0] + reverse_table
    
    return ''.join(map(str, table))