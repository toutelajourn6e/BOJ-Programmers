def solution(s):
    ans = list(map(int, s.split()))
    v = min(ans), max(ans)
    return ' '.join(map(str, v))