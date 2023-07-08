def solution(numbers, target):
    n = len(numbers)
    
    def dfs(depth, total):
        if depth == n:
            return 1 if total == target else 0
        
        result = 0
        result += dfs(depth+1, total + numbers[depth])
        result += dfs(depth+1, total - numbers[depth])
        
        return result
    
    return dfs(0, 0)
        
