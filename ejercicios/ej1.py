def sum_men_13(list):
    result = 0
    for i in list:
        if i < 13:
            result += i
    return result