from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque()
    cur_weight = 0
    time = 0
    
    while truck_weights or bridge:
        if bridge and time == bridge[0][0]:
            out = bridge.popleft()
            cur_weight -= out[1]
            continue
        if not bridge or (truck_weights and cur_weight + truck_weights[0] <= weight):
            enter = truck_weights.popleft()
            cur_weight += enter
            bridge.append((time + bridge_length, enter))
        time += 1 
    return time + 1