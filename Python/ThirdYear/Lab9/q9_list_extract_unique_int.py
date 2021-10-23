# Lab 9 Q9

# Go through list and extract only unique int

my_list = [1, 4, 5.5, 'da', 4, "aa"]
unique_int_set = set()

for i in my_list:
    if type(i) == int:
        unique_int_set.add(i)

print(unique_int_set)

