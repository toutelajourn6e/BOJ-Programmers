def check_prime(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(4, n+1):
        if not check_prime(i):
            answer += 1
    return answer
        
        

        