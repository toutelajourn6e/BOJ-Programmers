import re, sys

t = int(sys.stdin.readline().rstrip())
a = [sys.stdin.readline().rstrip() for _ in range(t)]
a.sort()
a = sorted(a, key = lambda x : (len(x), sum(list(map(int, re.findall('\d', x))))))

for i in a:
    sys.stdout.write(str(i) + '\n')