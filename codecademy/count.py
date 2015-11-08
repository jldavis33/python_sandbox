# Define a function called count that has two arguments called sequence and item.
# Return the number of times the item occurs in the list

# The item you input may be an integer, string, float, or even another list!


def count(sequence, item):
    num_count = 0
    for x_item in sequence:
        if x_item == item:
            num_count += 1

    # return num of items that occur in list
    return num_count

# my_list = [1, 2, 1, 2, 3, 1]
my_list_2 = [[2, 3], 2, 1, 2, [2, 3], 1]
print(count(my_list_2, [2, 3]))
