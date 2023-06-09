def solution(s):
    ans = [i.capitalize() for i in s.split(" ")]
    return ' '.join(ans)