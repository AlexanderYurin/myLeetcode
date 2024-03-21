d = {0: 0, 1: 1, 2: 1}

def fib(num):
    if num in d:
        return d[num]
    else:
        d[num] = fib(num - 1) + fib(num - 2)

    return d[num]
    # if num == 0:
    #     return 0
    # if num <= 2:
    #     return 1
    # return fib(num - 1) + fib(num - 2)
assert fib(10) == 55