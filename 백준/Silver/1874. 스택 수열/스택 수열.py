import sys
t = int(sys.stdin.readline())

stack = [0]
record = list()
index = 1

for _ in range(t):
    a = int(sys.stdin.readline())
    
    if a > stack[-1]:
        if index > a:
            print('NO')
            sys.exit()
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


for i in record:
    print(i)
    