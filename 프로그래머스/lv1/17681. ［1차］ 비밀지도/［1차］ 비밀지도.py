def solution(n, arr1, arr2):
    bin_map = []
    ans = []
    
    for i, j in zip(arr1, arr2):
        result = i | j
        bin_map.append(bin(result)[2:].zfill(n))
        
    for k in bin_map:
        a = k.replace('1', '#').replace('0', ' ')
        ans.append(a)
        
    return ans