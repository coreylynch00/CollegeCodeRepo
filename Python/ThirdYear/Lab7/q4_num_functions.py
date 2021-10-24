# Lab 7 Q4

numbers = []
for i in range(0, 5):
    number = int(input("Please enter a number: "))
    numbers.append(number)


def average_list(lst):
    avg = sum(lst) / len(lst)
    print(f"\nAverage = {avg:.2f}")


def max_list(lst):
    maximum = max(lst)
    print(f"Maximum = {maximum}")


def min_list(lst):
    minimum = min(lst)
    print(f"Minimum = {minimum}")


def sort_list(lst):
    print(f"Original = {lst}")
    sorty = sorted(lst)
    print(f"Sorted = {sorty}")


def sum_list(lst):
    summ = sum(lst)
    print(f"Sum = {summ}")


average_list(numbers)
max_list(numbers)
min_list(numbers)
sort_list(numbers)
sum_list(numbers)
