from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
game_map = [[0] * (n+1) for _ in range(n+1)]
game_map[1][1] = -1
k = int(input())

for _ in range(k):
    x, y = map(int, input().split())
    game_map[x][y] = 1
    
L = int(input())
moves = {}

for _ in range(L):
    a, b = input().split()
    moves[a] = b
      # 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
direction = 0
count = 0
head = (1, 1)
trace = deque()
trace.append(head)

while True:
    h_nx = head[0] + dx[direction]
    h_ny = head[1] + dy[direction]
    
    if 0 < h_nx <= n and 0 < h_ny <= n and game_map[h_nx][h_ny] >= 0:
        count += 1
        if game_map[h_nx][h_ny] == 1:
            game_map[h_nx][h_ny] = -1
            head = (h_nx, h_ny)
            trace.append(head)
            
        elif game_map[h_nx][h_ny] == 0:
            game_map[h_nx][h_ny] = -1
            head = (h_nx, h_ny)
            trace.append(head)
            tail = trace.popleft()
            game_map[tail[0]][tail[1]] = 0
    else:
        count += 1
        break   
    
    if str(count) in moves:
        if moves[str(count)] == 'L':
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4
        
        
print(count)

