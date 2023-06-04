n, k = map(int, input().split())
arr = list(map(int, input().split()))
each = 0
max_v = 0
for i in range(k):
    each += arr[i]
    
max_v = each

for i in range(k, n):
    each += arr[i]
    each -= arr[i-k]
    max_v = max(max_v, each)
    
print(max_v)