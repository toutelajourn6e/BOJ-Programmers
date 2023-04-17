from string import ascii_lowercase
import sys

S = sys.stdin.readline().rstrip()
alpha = list(ascii_lowercase)
ans = [0]*26

for i in S:
    ans[(alpha.index(i))] += 1
    
print(' '.join(map(str, ans)))

