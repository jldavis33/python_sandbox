
alpha = list('abcdefghijklmnopqrstuvwxyz')

# Basic way of iterating by using a count variable
count = 0
for letter in alpha:
    print('{}: {}'.format(count, letter))
    count += 1

# Using 'enumerate()' it iterate
for index, letter in enumerate(alpha):
    print('{}: {}'.format(index, letter))

# Unpacking a tuple while using 'enumerate()' to iterate over a list
for step in enumerate(alpha):
    print('{}: {}'.format(*step))


# CODE CHALLENGE
# Create a function 'combo()' that combines two lists together where the same indexed item in each
# is combined into a list of tuples

def combo(list1, list2):
    combo_list = []

    for i, _ in enumerate(list1):
        combo_list.append((list1[i], list2[i]))

    print(combo_list)
    return combo_list

combo([1, 2, 3], ['a', 'b', 'c'])
