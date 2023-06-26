from collections import Counter

def solution(participant, completion):
    person = Counter(participant) - Counter(completion)
    return list(person.keys())[0]
    