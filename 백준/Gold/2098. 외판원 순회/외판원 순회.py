def tsp(n, w):
    INF = int(1e9)
    dp = [[None] * (1 << n) for _ in range(n)]
    visited_all = (1 << n) - 1
    
    def find(last, visit):
        if visit == visited_all:
            return w[last][0] or INF
        
        if dp[last][visit] is not None:
            return dp[last][visit]
        
        temp = INF
        for left_city in range(n):
            if visit & (1 << left_city) == 0 and w[last][left_city] != 0:
                temp = min(temp, find(left_city, visit | (1 << left_city)) + w[last][left_city])
                
        dp[last][visit] = temp
        return temp
    
    
    return find(0, 1)
    
n = int(input())
w = []

for _ in range(n):
    w.append(list(map(int, input().split())))
    
print(tsp(n, w))           