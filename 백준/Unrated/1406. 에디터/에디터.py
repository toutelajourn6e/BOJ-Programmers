import sys

s = sys.stdin.readline().rstrip()
t = int(sys.stdin.readline())

lstack = [i for i in s]
rstack = list()

for _ in range(t):
    cmd = sys.stdin.readline().rstrip().split()
    
    if cmd[0] == 'L':
        if not lstack:
            pass
        else:
            rstack.append(lstack[-1])
            del lstack[-1]
    
    elif cmd[0] == 'D':
        if not rstack:
            pass
        else:
            lstack.append(rstack[-1])
            del rstack[-1]
    
    elif cmd[0] == 'B':
        if not lstack:
            pass
        else:
            del lstack[-1]
    
    elif cmd[0] == 'P':
        lstack.append(cmd[1])
        
rstack = rstack[::-1]
print(''.join(lstack + rstack))
        
