import re

def solution(my_string):
    answer = re.findall('[\d]+', my_string)
    sum = 0
    for i in answer:
        sum += int(i)
    return sum