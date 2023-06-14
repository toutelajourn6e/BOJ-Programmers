def solution(n):
    bin_n = bin(n)[2:].count('1')
    
    while n <= 1000000:
        n += 1
        new_bin_n = bin(n)[2:].count('1')
        if new_bin_n == bin_n:
            return int(bin(n)[2:], 2)