# Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

# Don't remove every occurrence, since you need to keep a single occurrence of a number.


def remove_duplicates(xlist):
    retval = []

    for item in xlist:
        if item not in retval:
            retval.append(item)

    return retval


print(remove_duplicates([1, 3, 5, 5, 'a', 'b', 'a']))