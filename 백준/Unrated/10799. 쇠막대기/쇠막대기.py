s = input()
s = s.replace('()','z')
stack = list()
ans = 0

for i in s:
    if i == '(':
        stack.append(i)
        ans += 1
    elif i == ')':
        stack.pop()
    elif i == 'z':
        ans += len(stack)
        
print(ans)