# LAB 4

A = ""
B = ""
C = ""
D = ""
E = ""

# Q1
# A OR B AND C OR D
if A or B or (B and C):
    print("")

# Q2
# A or B or C and D
if A or B or (C and D):
    print("")

# Q3
# A or B or C and D or E
if A or B or E or (C and D):
    print("")

# Q4
# notA and B or notC and D
if ((not A) and B) or ((not C) and D):
    print("")

# Q5
# A and B or notC
if (A and B) or (not C):
    print("")
