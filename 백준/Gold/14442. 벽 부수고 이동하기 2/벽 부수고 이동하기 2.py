from collections import deque
import sys 
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())

grid = [[int(i) for i in input().rstrip()] for _ in range(n)]
dist = [[[0] * m for _ in range(n)] for _ in range(k+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1

def bfs(x, y, count):
    
    while q:
        x, y, count = q.popleft()
        
        if x == n-1 and y == m-1:
            return dist[count][x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and dist[count][nx][ny] == 0:
                    q.append((nx, ny, count))
                    dist[count][nx][ny] = dist[count][x][y] + 1
                    
                if grid[nx][ny] == 1 and count < k and dist[count+1][nx][ny] == 0:
                    dist[count+1][nx][ny] = dist[count][x][y] + 1
                    q.append((nx, ny, count+1))
                
    return -1
    

print(bfs(0,0,0))
