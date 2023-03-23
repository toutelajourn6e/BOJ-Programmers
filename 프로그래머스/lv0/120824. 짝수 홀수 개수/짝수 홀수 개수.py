def solution(num_list):
    odd = list()
    even = list()
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return [len(even), len(odd)]