def solution(numbers):
    rev_num = sorted(numbers, reverse=True)
    if rev_num[0] * rev_num[1] > rev_num[-1] * rev_num[-2]:
        return rev_num[0] * rev_num[1]
    else:
        return rev_num[-1] * rev_num[-2]