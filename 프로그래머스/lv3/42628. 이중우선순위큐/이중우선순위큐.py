import heapq as hq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            hq.heappush(min_heap, num)
            hq.heappush(max_heap, -num)
        elif min_heap:
            if num == -1:
                hq.heappop(min_heap)
            else:
                target = -hq.heappop(max_heap)
                min_heap.remove(target)
    
    return [0, 0] if not min_heap else [max(min_heap), min(min_heap)]