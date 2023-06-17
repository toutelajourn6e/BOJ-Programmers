import sys
sys.setrecursionlimit(10**6)

def find_room(num, hotel):
    if not num in hotel:
        hotel[num] = num + 1
        return num
    else:
        hotel[num] = find_room(hotel[num], hotel)
        return hotel[num]

def solution(k, room_number):
    hotel = {}
    result = []
    
    for num in room_number:
        result.append(find_room(num, hotel))
        
    return result
            