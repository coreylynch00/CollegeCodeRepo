# Lab 9 Q2

# Find the number of items that are repeated more than once in the list


def my_function(my_list):
    my_set = set(my_list)
    return len(my_list) - len(my_set)

