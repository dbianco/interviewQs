
"""
This function bring back if it is posible to achieve the objective with/
 any of the numbers by adding them a certain number of times
"""

def groupSum(list, target):
    for num in list:
        acumulador = 0
        while acumulador < target:
            acumulador += num
        if acumulador == target:
            return True
    return False

"""
And this function bring back if it is posible with a group of numbers/
without repeating (brute force... very brute)
"""

def groupSum3elem(list, target):
    if list[0] + list[1] + list[2] == target:
        return True
    elif list[0] + list[1]== target:
        return True
    elif list[0] + list[2] == target:
        return True
    elif list[1] + list[2] == target:
        return True
    else:
        return False
