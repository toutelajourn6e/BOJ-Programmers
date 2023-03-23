def solution(sides):
    longest = max(sides)
    sides.remove(longest)
    
    if sum(sides) > longest:
        return 1
    else:
        return 2