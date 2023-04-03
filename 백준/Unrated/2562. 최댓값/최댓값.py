answer = list()

for i in range(9):
    num = int(input())
    answer.append(num)

print(max(answer))
print(answer.index(max(answer))+1)