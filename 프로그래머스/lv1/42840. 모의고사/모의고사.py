def solution(answers):
    score = [0, 0, 0]
    ans_1 = [1, 2, 3, 4, 5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for index, num in enumerate(answers):
        index_1 = index % 5
        index_2 = index % 8
        index_3 = index % 10
        
        if ans_1[index_1] == num:
            score[0] += 1
        if ans_2[index_2] == num:
            score[1] += 1
        if ans_3[index_3] == num:
            score[2] += 1
            
    return [i for i in [1, 2, 3] if score[i-1] == max(score)]