def solution(my_string):
    answer = list()
    for i in my_string:
        if not i in answer:
            answer.append(i)
    return ''.join(answer)