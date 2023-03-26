def solution(babbling):
    ong_r_2 = ['aya', 'ye', 'woo', 'ma']
    ong_dic = dict()
    answer = 0
    
    for i in ong_r_2:
        ong_dic[i] = True
        for j in ong_r_2:
            if i != j:
                j = i + j
                ong_dic[j] = True
            for k in ong_r_2:
                if k != i and k != j:
                    k = j + k
                    ong_dic[k] = True
                for n in ong_r_2:
                    if n != i and n != j and n != k:
                        n = k + n
                        ong_dic[n] = True
    
    for l in babbling:
        if l in ong_dic.keys():
            answer += 1
    return answer