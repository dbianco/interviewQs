import random


"""def createarray():
    numbers = []
    for _ in range(random.randint(0,10)):
        numbers.append(random.randint(0, 20))
    return numbers"""


def sum_men_13(list):
    result = 0
    for i in list:
        if i < 13:
            result += i
    return result
