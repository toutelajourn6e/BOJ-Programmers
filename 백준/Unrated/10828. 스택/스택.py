import sys

t = int(sys.stdin.readline())
stack = list()

for _ in range(t):
    a = sys.stdin.readline().split()
    cmd = a[0]
    
    if cmd == 'push':
        b = int(a[1])
        stack.append(b)
        
    elif cmd == 'pop':
        print(stack.pop() if stack else -1)
        
    elif cmd == 'size':
        print(len(stack))
        
    elif cmd == 'empty':
        print(0 if stack else 1)
            
    elif cmd == 'top':
        print(stack[-1] if stack else -1)