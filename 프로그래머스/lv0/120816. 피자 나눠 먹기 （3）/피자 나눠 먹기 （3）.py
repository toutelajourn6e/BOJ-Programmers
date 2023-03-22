def solution(slice, n):
    if slice == n or n < slice:
        return 1
    elif n % slice == 0:
        return n // slice
    else:
        return (n // slice) + 1