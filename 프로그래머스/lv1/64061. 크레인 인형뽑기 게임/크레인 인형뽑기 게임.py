def solution(board, moves):
    stack = []
    result = 0
    
    for move in moves:
        for i in range(len(board)):
            doll = board[i][move-1]
            if doll:
                if stack and doll == stack[-1]:
                    board[i][move-1] = 0
                    stack.pop()
                    result += 2
                else:
                    stack.append(doll)
                    board[i][move-1] = 0
                break
                
    return result