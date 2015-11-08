# Define a function called purify that takes in a list of numbers,
# removes all odd numbers in the list, and returns the result.


def purify(num_list):
    clean_list = []
    for num in num_list:
        if num % 2 == 0:
            clean_list.append(num)
    return clean_list

print(purify([1, 2, 3, 4, 5, 6, 7, 8]))
