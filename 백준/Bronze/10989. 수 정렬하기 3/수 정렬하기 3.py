import sys

t = int(sys.stdin.readline().rstrip())
a = [0] * 10001

for i in range(t):
    data = int(sys.stdin.readline().rstrip())
    a[data] += 1
    
for index, i in enumerate(a):
    if i:
        for j in range(i):
            sys.stdout.write(str(index) + '\n')