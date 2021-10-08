# Lab 5 Q3

# Calculate discount on product given quantity ordered

PRICE = 99
quantity = int(input("Enter quantity you would like to order: "))
total = PRICE * quantity

if 1 <= quantity <= 9:
    print(f"\n\tDiscount: 0% \tTotal: {total:.2f} \tQuantity: {quantity}")
elif 10 <= quantity <= 19:
    discount = "20%"
    disc_total = total - (0.2 * total)
    print(f"\n\tTotal Before Discount: {total:.2f} \tDiscount: {discount} \tTotal: {disc_total:.2f} \tQuantity: "
          f"{quantity}")
elif 20 <= quantity <= 49:
    discount = "30%"
    disc_total = total - (0.3 * total)
    print(f"\n\tTotal Before Discount: {total:.2f} \tDiscount: {discount} \tTotal: {disc_total:.2f} \tQuantity: "
          f"{quantity}")
elif 50 <= quantity <= 99:
    discount = "40%"
    disc_total = total - (0.4 * total)
    print(f"\n\tTotal Before Discount: {total:.2f} \tDiscount: {discount} \tTotal: {disc_total:.2f} \tQuantity: "
          f"{quantity}")
elif quantity >= 100:
    discount = "50%"
    disc_total = total - (0.5 * total)
    print(f"\n\tTotal Before Discount: {total:.2f} \tDiscount: {discount} \tTotal: {disc_total:.2f} \tQuantity: "
          f"{quantity}")
else:
    print("That is not a valid quantity.")
