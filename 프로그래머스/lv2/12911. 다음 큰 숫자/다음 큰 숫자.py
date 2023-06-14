def solution(n):
    bin_n = bin(n).count('1')
    
    while True:
        n += 1
        new_bin_n = bin(n).count('1')
        if new_bin_n == bin_n:
            return n