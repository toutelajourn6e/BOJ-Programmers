n = int(input())
a = list(map(int, input().split()))
stack = [0]
ans = [-1] *n
freq = {}
for j in a:
    try:
        freq[j] += 1
    except:
        freq[j] = 0
    
for i in range(1, n):
    if not stack:
        stack.append(i)
    while stack and freq[a[stack[-1]]] < freq[a[i]]:
        ans[stack.pop()] = a[i]
    stack.append(i)
    
print(' '.join(map(str, ans)))