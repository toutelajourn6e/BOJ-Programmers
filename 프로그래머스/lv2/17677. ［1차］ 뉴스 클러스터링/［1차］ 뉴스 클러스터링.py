from collections import defaultdict
import re

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    A, B = [], []
    for i in range(len(str1)-1):
        temp = str1[i] + str1[i+1]
        if len(re.sub('[^a-zA-Z]', '', temp)) == 2:
            A.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        temp = str2[i] + str2[i+1]
        if len(re.sub('[^a-zA-Z]', '', temp)) == 2:
            B.append(str2[i]+str2[i+1])
       
    dic_A, dic_B = defaultdict(int), defaultdict(int)
    
    for word in A:
        dic_A[word] += 1
    for word in B:
        dic_B[word] += 1
        
    intersection = []
    union = []
    
    for i in set(A).union(set(B)):
        min_v = min(dic_A[i], dic_B[i])
        max_v = max(dic_A[i], dic_B[i])
        for _ in range(min_v):
            intersection.append(i)
        for _ in range(max_v):
            union.append(i)
    
    if not len(intersection) and not len(union):
        return 65536
    else:
        return int((len(intersection) / len(union)) * 65536)