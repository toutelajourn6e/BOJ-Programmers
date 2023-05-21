from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

grid = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1

def bfs(x, y, count):
    
    while q:
        x, y, count = q.popleft()
        
        if x == n-1 and y == m-1:
            return dist[x][y][count]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and dist[nx][ny][count] == 0:
                    q.append((nx, ny, count))
                    dist[nx][ny][count] = dist[x][y][count] + 1
                    
                if grid[nx][ny] == 1 and count == 0 and dist[nx][ny][count] == 0:
                    dist[nx][ny][count+1] = dist[x][y][count] + 1
                    q.append((nx, ny, count+1))
                
    return -1
    

print(bfs(0,0,0))