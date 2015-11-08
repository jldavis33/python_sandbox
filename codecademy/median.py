# Write a function to find the median of a list.


def median(list_of_int):
    retval = None
    list_len = len(list_of_int)

    # sort the list
    list_of_int.sort()

    # if list has even num, find average of middle two
    if list_len % 2 == 0:
        a = list_of_int[int(list_len/2 - 1)]
        b = list_of_int[int(list_len/2)]

        retval = (a + b) / 2.0

    # else get median
    else:
        retval = list_of_int[int(round(list_len/2))]

    return retval

int_list = [4, 5, 5, 4]
print(median(int_list))

