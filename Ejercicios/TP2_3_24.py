'''/* Given an array of ints, is it possible to choose a group of some of the ints,
    such that the group sums to the given target?
    Sample: groupSum([2, 4, 8], 10) → true
            groupSum([2, 4, 8], 14) → true
            groupSum([2, 4, 8], 9) → false
     */'''

def groupSum(a,b):
    result= 0
    if sum(a[::]) == b or sum(a[0:2])== b or sum(a[1:3])== b or a[0]+a[2]== b:
        result = True
    else:
        result = False
    
    return result

print(groupSum([2, 5, 18],23))


def groupSum2(a,b):
    n = len(a)
    if sum(a[::]) == b:
        result = True
    else:
        for i in a:
            if b - i in a:
                result = True
            else:
                result = False
    return result

print(groupSum2([2,4,8,6],20))



