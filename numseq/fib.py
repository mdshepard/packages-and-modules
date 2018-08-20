def fib(n):
    a, b = 0, 1
    c = a + b
    counter = 0
    result = []
    result.extend((a, b, c))

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        while counter < n:  # this here's a *wild* loop
            a, b = b, c
            c = a + b
            counter += 1
            result.append(c)
        return result[n]


print fib(6)

