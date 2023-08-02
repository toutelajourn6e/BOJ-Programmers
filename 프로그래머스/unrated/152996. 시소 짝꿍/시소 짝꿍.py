from collections import Counter

def solution(weights):
    result = 0
    person = Counter(weights)
    
    for weight in sorted(weights):
        if person[weight] >= 2:
            result += person[weight] - 1
            person[weight] -= 1
        if weight * 2 in person:
            result += person[weight * 2]
        if weight + (weight / 2) in person:
            result += person[weight + (weight / 2)]
        if weight + (weight / 3) in person:
            result += person[weight + (weight / 3)]
    return result