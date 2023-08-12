# 게임판이 다 찼을 때, x가 o보다 갯수가 많을 때, o가 x보다 2개 더 많을 때.
def check(board, sign):
    for i in range(3): # 가로
        if board[i] == sign * 3: return 1
    
    for i in range(3): # 세로
        temp = ''
        for j in range(3):
            temp += board[j][i]
        if temp == sign * 3: return 1
    
    if board[0][0] + board[1][1] + board[2][2] == sign * 3 or board[0][2] + board[1][1] + board[2][0] == sign * 3: return 1
    
    return 0


def solution(board):
    O, X = 0, 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.': is_full = False
            elif board[i][j] == 'O': O += 1
            else: X += 1
            
    if O >= X + 2 or X >= O + 1: return 0

    if check(board, 'O') and check(board, 'X'): return 0
    elif check(board, 'O') and O != X + 1: return 0
    elif check(board, 'X') and X != O: return 0

    return 1