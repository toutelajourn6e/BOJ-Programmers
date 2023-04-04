a = list(map(int, input().split()))

dic = {
    'ascending': [1,2,3,4,5,6,7,8],
    'descending': [8,7,6,5,4,3,2,1]   
}

if a == dic['ascending']:
    print('ascending')
elif a == dic['descending']:
    print('descending')
else:
    print('mixed')