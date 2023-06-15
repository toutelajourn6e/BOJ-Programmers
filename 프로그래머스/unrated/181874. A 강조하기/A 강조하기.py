def solution(myString):
    ans = ''
    for i in myString:
        if i in ['a', 'A']:
            ans += i.upper()
        else:
            ans += i.lower()
    return ans