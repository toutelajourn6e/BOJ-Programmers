def solution(my_str, n):
    ans = []
    
    while my_str:
        ans.append(my_str[:n])
        my_str = my_str[n:]
        
    return ans
