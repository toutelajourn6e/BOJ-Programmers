def rotate(query, matrix):
    x1, y1, x2, y2 = query
    first = matrix[x1][y1]
    min_v = first
    
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k+1][y1]
        min_v = min(min_v, matrix[k+1][y1])
        
    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k+1]
        min_v = min(min_v, matrix[x2][k+1])
        
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k-1][y2]
        min_v = min(min_v,matrix[k-1][y2])

    for k in range(y2, y1, -1):
        matrix[x1][k] = matrix[x1][k-1]
        min_v = min(min_v, matrix[x1][k-1])
        
    matrix[x1][y1+1] = first
        
    return min_v
    
    
    

def solution(r, c, queries):
    result = []
    matrix = [[(i-1)*c+j for j in range(c+1)] for i in range(r+1)]
    
    for query in queries:
        result.append(rotate(query, matrix))
        
    return result
    
    
    
    
    
    