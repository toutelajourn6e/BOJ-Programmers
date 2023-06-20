from math import gcd

def get_lcm(a, b):
    g = gcd(a, b)
    lcm = a * b // g
    return lcm

def solution(arr):
    arr.sort()
    temp = arr[0]
    
    for i in range(len(arr)-1):
        temp = get_lcm(temp, arr[i+1])
        
    return temp
        