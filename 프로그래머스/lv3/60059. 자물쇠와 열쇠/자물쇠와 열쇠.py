import copy

def check(offset, k, ex_board):
    for i in range(offset, k - offset):
        for j in range(offset, k - offset):
            if ex_board[i][j] != 1:
                return False
    return True

def rotate(key, m):
    new = copy.deepcopy(key)
    for i in range(m):
        for j in range(m):
            new[j][m-1-i] = key[i][j]
    return new

def solution(key, lock):
    n = len(lock)
    m = len(key)
    offset = m - 1
    ex_board = [[0] * (offset * 2 + n) for _ in range((offset * 2 + n))]
    k = len(ex_board)
    
    for i in range(offset, k - offset):
        for j in range(offset, k - offset):
            ex_board[i][j] = lock[i-offset][j-offset]
            
    for i in range(k - offset):
        for j in range(k - offset):
            for l in range(4):
                for a in range(m):
                    for b in range(m):
                        ex_board[i+a][j+b] += key[a][b]
                result = check(offset, k, ex_board)
                if result:
                    return True
                for a in range(m):
                    for b in range(m):
                        ex_board[i+a][j+b] -= key[a][b]
                key = rotate(key, m)
    return False
                    