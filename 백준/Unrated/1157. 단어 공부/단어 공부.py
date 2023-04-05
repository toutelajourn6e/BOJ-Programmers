from collections import Counter

a = list(input().upper())

count_item = Counter(a)
if len(count_item) == 1:
    print(count_item.most_common(n=1)[0][0])
else:    
    top2 = count_item.most_common(n=2)

    if top2[0][1] == top2[1][1]:
        print('?')
    else:
        print(top2[0][0])