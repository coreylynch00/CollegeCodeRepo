a = int(input("Number ==> "))
b = int(input("Number ==> "))
c = int(input("Number ==> "))

if a > b and a > c:
    print(a , "is the biggest number")
elif b > a and b > c:
    print(b, "is the biggest number")
elif c > a and c > b:
    print(c, "is the biggest number")
elif a == b and a > c:
    print(a , "is the biggest number and appears twice")
elif a == c and a > b:
    print(a, "is the biggest number and appears twice")
elif b == c and b > a:
    print(b, "is the biggest number and appears twice")
else:
    print("All three numbers are the same")

