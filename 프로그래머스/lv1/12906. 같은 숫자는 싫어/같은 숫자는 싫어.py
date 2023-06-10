def solution(arr):
    ans = [-1]
    for i in range(len(arr)):
        if arr[i] != ans[-1]:
            ans.append(arr[i])
    return ans[1:]