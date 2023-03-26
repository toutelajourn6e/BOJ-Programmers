def solution(my_string, num1, num2):
    temp = my_string
    my_string = ','.join(my_string).split(',')
    my_string[num1] = temp[num2]
    my_string[num2] = temp[num1]
    my_string = ''.join(my_string)
    return my_string

