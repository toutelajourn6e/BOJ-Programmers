def solution(M, N):
    if M == 1 and N == 1:
        return 0
    else:
        return (M - 1) + (M * (N - 1))