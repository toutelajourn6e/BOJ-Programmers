def solution(phone_number):
    ans = list(phone_number)
    ans[:-4] = '*' * len(ans[:-4])
    return ''.join(ans)