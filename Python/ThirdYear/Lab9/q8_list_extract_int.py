# Lab 9 Q8

# Go through list and extract only int

my_list = [1, 2, "Corey", 69, "Hello World", 7.9]
int_list = []

for i in my_list:
    if type(i) == int:
        int_list.append(i)

print(my_list)
print(int_list)