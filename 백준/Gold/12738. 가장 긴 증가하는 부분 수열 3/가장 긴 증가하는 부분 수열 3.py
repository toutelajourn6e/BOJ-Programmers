from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
LIS = [arr[0]]

for i in arr:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        idx = bisect_left(LIS, i)
        LIS[idx] = i
        
print(len(LIS))
