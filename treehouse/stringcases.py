# Handy functions:
# .upper() - uppercases a string
# .lower() - lowercases a string
# .title() - titlecases a string
# There is no function to reverse a string.
# Maybe you can do it with a slice?


def stringcases(string):
    a_tuple = string.upper(), string.lower(), string.title(), string[::-1]
    print(a_tuple)
    return a_tuple


stringcases('Joshua')
