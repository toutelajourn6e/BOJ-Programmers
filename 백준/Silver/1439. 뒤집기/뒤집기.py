import re
s = input()
count_1 = len(re.findall('1+', s))
count_0 = len(re.findall('0+', s))

print(min(count_1, count_0))