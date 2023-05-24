from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

LIS = []
LIS_idx = []

for i in arr:
    if not LIS or LIS[-1] < i:
        LIS.append(i)
        LIS_idx.append((len(LIS)-1, i))
    else:
        LIS[bisect_left(LIS, i)] = i
        LIS_idx.append((bisect_left(LIS, i), i))

        
result = []
length = len(LIS)-1

for i in range(len(LIS_idx)-1, -1, -1):
    if LIS_idx[i][0] == length:
        result.append(LIS_idx[i][1])
        length -= 1
        
print(len(LIS))
print(*result[::-1])
        