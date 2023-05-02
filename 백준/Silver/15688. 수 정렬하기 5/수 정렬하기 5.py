import sys

t = int(sys.stdin.readline().rstrip())
a = [int(sys.stdin.readline().rstrip()) for _ in range(t)]

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return
    m = n // 2
    g1 = a[:m]
    g2 = a[m:]
    
    merge_sort(g1)
    merge_sort(g2)
    
    i = 0; j = 0; k = 0;
    
    while i < len(g1) and j < len(g2):
        if g1[i] < g2[j]:
            a[k] = g1[i]
            i += 1
            k += 1
        else:
            a[k] = g2[j]
            j += 1
            k += 1
            
    while i < len(g1):
        a[k] = g1[i]
        i += 1
        k += 1
        
    while j < len(g2):
        a[k] = g2[j]
        j += 1
        k += 1
        
    return a

merge_sort(a)

for l in a:
    sys.stdout.write(str(l) + '\n')