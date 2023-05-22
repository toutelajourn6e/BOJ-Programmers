import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
wood = list(map(int, input().rstrip().split()))

start = 0
end = max(wood)
result = 0

while start <= end:
    temp = 0
    mid = (start + end) // 2
    for i in wood:
        if i > mid:
            temp += i - mid
    if temp < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)
        