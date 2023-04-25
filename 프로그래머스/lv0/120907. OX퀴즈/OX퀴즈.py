def solution(quiz):
    result = []
    for i in quiz:
        i = i.split(' = ')
        if eval(i[0]) == int(i[1]):
            result.append('O')
        else:
            result.append('X')
            
    return result