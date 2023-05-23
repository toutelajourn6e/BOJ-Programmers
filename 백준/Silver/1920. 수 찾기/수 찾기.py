def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
   
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return 0

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
find = list(map(int, input().split()))

for i in find:
    print(binary_search(arr, i))