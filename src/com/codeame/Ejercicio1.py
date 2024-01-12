import sys

def sum13(nums):

    return sum([num for num in nums if num < 13])


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python script_name.py num1 num2 num3 ...")
        sys.exit(1)

    # Convert command line arguments to integers
    nums = [int(arg) for arg in sys.argv[1:]]

    # Call the function with the provided numbers
    result = sum13(nums)

    # Display the result
    print("Sum of numbers except 13 and greater:", result)