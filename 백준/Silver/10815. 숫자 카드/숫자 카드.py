n = int(input())
have = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
count = {}

for i in have:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        
for j in find:
    if j in count:
        print(count[j], end=' ')
    else:
        print(0, end=' ')