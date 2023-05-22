def promising(i):
    for k in range(i):
        if row[i] == row[k] or abs(row[i] - row[k]) == abs(i - k):
            return False
        
    return True


def n_queen(i):
    global cnt
    if i == n:
        cnt += 1
        return
    else:
        for j in range(n):
            row[i] = j
            if promising(i):
                n_queen(i+1)
                
                
n = int(input())
row = [0] * n
cnt = 0

n_queen(0)

print(cnt)