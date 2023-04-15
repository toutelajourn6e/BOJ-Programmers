from string import ascii_lowercase

alphabet = list(ascii_lowercase)
s = input()

for i in alphabet:
    if i in s:
        print(s.find(i), end=' ')
    else:
        print(-1, end=' ')