def solution(n):
    ans = 0
    cnt = 0
    while True:
        cnt += 1
        if '3' in str(cnt) or cnt % 3 == 0:
            continue
        ans += 1
        if ans == n:
            break
    return cnt