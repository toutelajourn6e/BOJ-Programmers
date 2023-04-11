
t = int(input())

stack = [0]
record = list()
index = 1
no = False
for _ in range(t):
    a = int(input())
    
    if a > stack[-1]:
        if index > a:
            no = True
            break
        while not a == stack[-1]:
            stack.append(index)
            record.append('+')
            index += 1
        stack.pop()
        record.append('-')
    elif a < stack[-1]:
        while not a == stack[-1]:
            stack.pop()
            record.append('-')
        stack.pop()
        record.append('-')
    elif a == stack[-1]:
        stack.pop()
        record.append('-')

if no == False:
    for i in record:
        print(i)
else:
    print('NO')
    