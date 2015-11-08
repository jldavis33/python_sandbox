# Define a function called product that takes a list of integers as
# input and returns the product of all of the elements in the list.


def product(list_of_int):
    retval = 1

    for num in list_of_int:
        try:
            retval *= int(num)
        except ValueError or TypeError:
            print("Error: Pass only a list of integers")
            return None

    return retval

print(product([3, 3, 5]))
