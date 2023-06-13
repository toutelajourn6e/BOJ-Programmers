def travel(start, edges, n, result):
    result.append(start)
    
    if len(result) == n + 1:
        return True
    
    for index, NEXT in enumerate(edges[start]):
        edges[start].remove(NEXT)
        if travel(NEXT, edges, n, result):
            return True
        edges[start].insert(index, NEXT)
        
    result.pop()
    return False



def solution(tickets):
    n = len(tickets)
    result = []
    edges = {}
    
    for departure, arrival in tickets:
        if departure not in edges:
            edges[departure] = []
        if arrival not in edges:
            edges[arrival] = []
        edges[departure].append(arrival)
        
    for i in edges:
        edges[i] = sorted(edges[i])
        
    travel('ICN', edges, n, result)
    
    return result