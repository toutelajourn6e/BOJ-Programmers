def solution(num_list):
    if len(num_list) > 10:
        return sum(num_list)
    else:
        sum_v = 1
        for i in num_list:
            sum_v *= i
        return sum_v