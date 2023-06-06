# 입력 (x 좌표, y 좌표, 0기둥 - 1보, 0삭제  - 1설치)
C = 0
S = 1

def impossible(result):
    for x, y, a in result:
        if a == C:
            if y != 0 and (x, y-1, C) not in result and (x-1, y, S) not in result and (x, y, S) not in result:
                return True
        else:
            if (x, y-1, C) not in result and (x+1, y-1, C) not in result and not ((x-1, y, S) in result and (x+1, y, S) in result):
                return True
    return False
                


def solution(n, build_frame):
    result = set()
    
    for x, y, a, b in build_frame:
        if b:
            result.add((x, y, a))
            if impossible(result):
                result.discard((x, y, a))
        else:
            result.discard((x, y, a))
            if impossible(result):
                result.add((x, y, a))
                
    ans = list(result)
    return sorted(ans, key = lambda x: (x[0], x[1], x[2]))
                    
                    
                    
                    