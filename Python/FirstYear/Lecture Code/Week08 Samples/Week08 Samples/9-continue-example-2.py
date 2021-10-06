food_i_do_not_like = ('sprouts', 'oysters', 'cabbage')
shopping_list = ''
while True:
    food_item = input('Food Item for shopping list (<RET> to finish): ').capitalize()
    if food_item == '':
        break
    if food_item.lower() in food_i_do_not_like:
        continue
    shopping_list += food_item + "\n"

print ("Shopping List")
print(shopping_list)
