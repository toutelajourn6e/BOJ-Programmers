from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(place):
    start = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append((i, j))
                
    for s in start:
        visited = [[False] * 5 for _ in range(5)]
        visited[s[0]][s[1]] = True
        board = [[0] * 5 for _ in range(5)]
        q = deque()
        q.append(s)
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False:
                    if place[nx][ny] == 'O':
                        board[nx][ny] = board[x][y] + 1
                        visited[nx][ny] = True
                        q.append((nx, ny))
                    if place[nx][ny] == 'P' and board[x][y] < 2:
                        return 0
    return 1    
           

def solution(places):
    result = []
    
    for place in places:
        result.append(bfs(place))
    
    return result