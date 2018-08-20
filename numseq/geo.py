"""functions dealing with geometric values for arguments"""

"""this squares n"""


def square(n):
    return n * n


"""this cubes n"""


def cube(n):
    return n ** 3


"""weren't never a booklearner"""


def triangle(n):
    result = []
    count = 1
    number = n
    result.append(number)
    while n > count:
        result.append(number - 1)
        number -= 1
        count += 1
    return sum(result)
