COFFEE = 2.20
TEA = 1.70
MILK = 1.65
menu = "Would you like " + \
       "\n\t1: Coffee" \
       "\n\t2: Tea" \
       "\n\t3: Milk" \
       "\n==> "
choice = int(input(menu))
cost = 0
if choice == 1:
    cost = COFFEE
elif choice == 2:
    cost = TEA
elif choice == 3:
    cost = MILK

print("That will be €" + str(cost))


