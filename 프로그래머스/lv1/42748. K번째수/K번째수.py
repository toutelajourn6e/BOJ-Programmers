def solution(array, commands):
    result = []
    for start, end, k in commands:
        result.append(sorted(array[start-1:end])[k-1])
    return result