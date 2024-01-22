
import unittest
"""Given three ints, a b c, one of them is small, one is medium and one is large.
    Return true if the three values are evenly spaced, so the difference between
    small and medium is the same as the difference between medium and large.
    Sample: evenlySpaced(2, 4, 6) → true
            evenlySpaced(4, 6, 2) → true
            evenlySpaced(4, 6, 3) → false"""

def evenlySpaced (a, b, c):     
    if a<b and a<c:
        small = a
        if b<c:
            medium = b
            large = c
        else: 
            large = b
            medium = c

    elif b<a and b<c:
        small= b
        if a<c:
            medium = a
            large = c
        else: 
            medium = c
            large = a
    else: 
        small= c
        if a<b:
            medium = a
            large = b
        else: 
            medium = b
            large = c

    if medium-small == large-medium:
        result = True
    else:
        result = False
           
    return result
print(evenlySpaced(2, 4, 6))                

def test():
    print("testeando... ")
    assert(evenlySpaced(2,4,6) == True), "ERROR"
    assert(evenlySpaced(4,6,2) == True), "ERROR"
    assert(evenlySpaced(4,6,3) == False), "ERROR"
    print("Pasó chango")

test()

class Test(unittest.TestCase):
    def test_(self):
        self.assertEqual(evenlySpaced(2, 4, 6), True)

if __name__ == '__main__':
    unittest.main()