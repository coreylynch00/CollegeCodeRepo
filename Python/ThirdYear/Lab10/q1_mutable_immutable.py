# Lab 10 Q1

# If collection is mutable, convert to immutable, otherwise return collection

# Uncomment a data struct to test if mutable/immutable
my_list = [1, 3, 4.5, "hello"]
# my_list = (1, 3, 4.5, "hello")
# my_list = {1, 3, 4.5, "hello"}


def mutable_check(data_struct):
    if type(data_struct) == list or type(data_struct) == set:
        immutable = tuple(data_struct)
        print("Mutable Data Struct, Converted to Tuple:\n", type(immutable), immutable)
    else:
        print("Already Immutable:\n", type(data_struct), data_struct)


mutable_check(my_list)
