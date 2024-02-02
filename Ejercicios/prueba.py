def sum(nums):
    suma = 0
    for i in nums:
        if i<13:
            suma += i
    return suma

def testing():
    print("Testeando....")
    assert sum([1,2,2,1,13,5]) == 11, "ERROR"
    assert sum([1,2,2,1,10]) == 16, "ERROR"
    assert sum([13,1,2,2,1]) == 6, "ERROR"
    assert sum([1,2,2,1,13,10,25]) == 16, "ERROR"
    assert sum([1,2,55,2,1,13,10,25,55]) == 16, "ERROR"
    assert sum([1,2,2,1,13,10,25,5,7]) == 28, "ERROR"
    print("Pasó señores")
    return 

testing()