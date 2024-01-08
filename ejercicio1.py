import random


def createarray():
    numbers = []
    for _ in range(random.randint(0,10)):
        numbers.append(random.randint(0, 20))
    return numbers


def main():
    result = 0
    numbers = createarray()
    for i in numbers:
        if i < 13:
            result += i
    for i in numbers:
        print(i)
    print("La suma de los numeros fue", result)


main()