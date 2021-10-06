with open("diy.txt") as data_source:
    for line in data_source:
        student_name = line.rstrip()
        class_group  = data_source.readline().rstrip()
        print(f"{student_name:15s} {class_group}")

