def solution(lottos, win_nums):
    bestcase = 0
    worstcase = 0
    win = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    for num in lottos:
        if num == 0:
            bestcase += 1
        elif num in win_nums:
            bestcase += 1
            worstcase += 1
            
    return [win[bestcase], win[worstcase]]