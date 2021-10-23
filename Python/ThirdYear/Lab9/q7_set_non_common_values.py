# Lab 9 Q7

# Two sets as input, returns only those values that were not common among both sets

def non_common(s1, s2):
    return s1 ^ s2

# ^ is an operator for XOR
# NOT (A intersect B)

s1 = {1, 2, 3, 4, 5, 6}

s2 = {10, 20, 30, 4, 5, 6}

print(non_common(s1, s2))
