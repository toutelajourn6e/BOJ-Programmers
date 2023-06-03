n, target = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
inter = 0
count = 0

for start in range(n):
    while inter < target and end < n:
        inter += arr[end]
        end += 1
    if inter == target:
        count += 1
    inter -= arr[start]
    
print(count)