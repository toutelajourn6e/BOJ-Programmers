solution = lambda array, n : sorted(array, key = lambda x:(abs(x-n),x))[0]