def solution(n):
    odd_list = list()
    for i in range(1, n + 1):
        if i % 2 == 1:
            odd_list.append(i)
    
    return odd_list
    