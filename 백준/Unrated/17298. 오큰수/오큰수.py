n = int(input())
a = list(map(int, input().split()))
stack = [0]

for i in range(1, n):
    if not stack:
        stack.append(i)
    while stack and a[stack[-1]] < a[i]:
        a[stack.pop()] = a[i]
    stack.append(i)

while stack:
    a[stack.pop()] = -1

print(' '.join(map(str, a)))