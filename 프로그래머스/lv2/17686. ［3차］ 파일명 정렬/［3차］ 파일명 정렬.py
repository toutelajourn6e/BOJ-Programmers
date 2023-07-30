def solution(files):
    result = []
    
    for idx, file in enumerate(files):
        tmp = []
        num = 0
        for i in range(len(file)):
            if file[i].isdigit():
                tmp.append(file[:i])
                num = i
                break
        for i in range(num, len(file)):
            if i == len(file)-1:
                tmp.append(file[num:])
                tmp.append((idx, ''))
                break
            if not file[i].isdigit():
                tmp.append(file[num:i])
                tmp.append((idx, file[i:]))
                break
        result.append(tmp)
     
    result.sort(key=lambda x: (x[0].lower(), int(x[1]), x[2][0]))
    return [''.join((x[0], x[1], x[2][1])) for x in result]          