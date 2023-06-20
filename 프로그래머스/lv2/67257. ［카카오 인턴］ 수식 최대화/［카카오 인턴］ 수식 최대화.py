from itertools import permutations
from collections import deque
import re

def solution(expression):
    operators = list(permutations(['*', '-', '+']))
    max_v = 0
    
    for operator in operators:
        temp = deque(re.split('([-+*])', expression))
        stack = []
        for o in operator:
            while temp:
                elem = temp.popleft()
                if elem == o:
                    stack.append(str(eval(stack.pop() + o + temp.popleft())))
                else:
                    stack.append(elem)
            else:   
                temp = deque(stack[:])
                stack.clear()
        else:
            v = int(temp.pop())
            max_v = max(max_v, abs(v))
    return max_v