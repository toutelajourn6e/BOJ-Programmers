S = input()
ans = ''

for i in S:
    if i.islower():
        a = ord(i) + 13
        if a > 122:
            a = 97 + (13 - (123 - ord(i)))
        a = chr(a)
        ans += a
    elif i.isupper():
        a = ord(i) + 13
        if a > 90:
            a = 65 + (13 - (91 - ord(i)))
        a = chr(a)
        ans += a
    else:
        ans += i
print(ans)