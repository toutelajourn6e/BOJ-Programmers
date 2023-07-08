from collections import defaultdict

def dfs(edges, path, visit):
    if path:
        to = path[-1]
        if edges[to]:
            path.append(edges[to].pop(0))
        else:
            visit.append(path.pop())
            
        dfs(edges, path, visit)
    
    return visit[::-1]

def solution(tickets):
    edges = defaultdict(list)
    
    for departure, arrival in tickets:
        edges[departure].append(arrival)
        
    for key in edges.keys():
        edges[key].sort()
        
    return dfs(edges, ['ICN'], [])