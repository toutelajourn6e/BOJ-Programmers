def solution(keyinput, board):
    move = [0,0]
    for i in keyinput:
        if i == 'left':
            if move[0] > -(board[0] // 2):
                move[0] -= 1
            else:
                continue
        elif i == 'right':
            if move[0] < board[0] // 2:
                move[0] += 1
            else:
                continue
        elif i == 'up':
            if move[1] < board[1] // 2:
                move[1] += 1
            else:
                continue
        elif i == 'down':
            if move[1] > -(board[1] // 2):
                move[1] -= 1
            else:
                continue
                
    return move
        