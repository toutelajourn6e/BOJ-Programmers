def solution(m, n, board):
    board = [[board[i][j] for j in range(n)] for i in range(m)]
    ans = 0
    check = set()
    
    def br():
        nonlocal check, ans
        for i in range(m):
            for j in range(n):
                if 0 <= i+1 < m and 0 <= j+1 < n and board[i][j] is not None:
                    block = board[i][j]
                    if board[i][j+1] == block and board[i+1][j] == block and board[i+1][j+1] == block:
                        check.add((i, j))
                        check.add((i , j+1))
                        check.add((i+1, j+1))
                        check.add((i+1, j))
        if check:
            ans += len(check)
            for i, j in check:
                board[i][j] = None
            check = set()
        else: return False

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] is not None:
                    max_row = 0
                    for k in range(i+1, m):
                        if board[k][j] is None and k == m-1:
                            if max_row > 0:
                                board[k][j] = board[i][j]
                                board[i][j] = None
                                break
                        elif board[k][j] is None:
                            max_row = max(max_row, k)
                        
                        elif board[i][j] is not None:
                            if max_row > 0:
                                board[max_row][j] = board[i][j]
                                board[i][j] = None
                                break

        if not br(): return False    
        
    br()
    return ans