t = int(input())

for i in range(t):
    answer = input().split('X')
    score = 0
    while ''in answer:
        answer.remove('')
    for j in answer:
        score += sum([k for k in range(1, len(j)+1)])
    print(score)