import heapq as hq
def solution(book_time):
    book_time.sort(key=lambda x: x[0])
    rooms = []
    ans = [1]
    cur = 0
    for enter, exit in book_time:
        enter = int(''.join(enter.split(':')))
        exit = list(map(int, exit.split(':')))
        exit[1] += 10
        if exit[1] >= 60:
            exit[0] += 1
            exit[1] %= 60
        if exit[1] < 10: 
            exit[1] = '0' + str(exit[1])
        else: 
            exit[1] = str(exit[1])
        exit = int(''.join(map(str, exit)))

        if not rooms:
            hq.heappush(rooms, exit)
            cur += 1
        else:
            while rooms:
                check = hq.heappop(rooms)
                if check > enter:
                    hq.heappush(rooms, check)
                    break
                else:
                    cur -= 1
            cur += 1
            ans.append(cur)
            hq.heappush(rooms, exit)
            
    return max(ans)          