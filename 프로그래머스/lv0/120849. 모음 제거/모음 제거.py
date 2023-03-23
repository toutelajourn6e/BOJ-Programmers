def solution(my_string):
    answer = ''
    vowel = ['a','e','i','o','u']
    
    for s in my_string:
        if not s in vowel:
            answer += s
    return answer