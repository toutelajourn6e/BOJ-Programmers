def solution(numbers):
    nums = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for index, i in enumerate(nums):
        numbers = numbers.replace(i, str(index))
        
    return int(numbers)
                