def solution(arr, n):
    leng = len(arr)
    if leng % 2:
        for i in range(0, leng, 2):
            arr[i] += n
    else:
        for i in range(1, leng, 2):
            arr[i] += n
    return arr