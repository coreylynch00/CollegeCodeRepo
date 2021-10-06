full_price_milk = float(input('How much is a litre of milk?'))
full_price_bread = float(input('How much is a loaf of bread?'))

litre_milk_bought = int(input('How many litres of milk did you buy?'))
loaves_bread_bought = int(input('How many loafs of bread did you buy?'))

reduced_milk = float(full_price_milk * 0.9)
reduced_bread = float(full_price_bread * 0.9)

total_milk = (reduced_milk * litre_milk_bought)
total_bread = (reduced_bread * loaves_bread_bought)
total_bill = total_milk + total_bread

print('\n')
print('Your Bill')
print('-' * 37)

print(f'Milk {litre_milk_bought:10}{reduced_milk:10.2f}{total_milk:10.2f}')
print(f'Bread {loaves_bread_bought:9}{reduced_bread:10.2f}{total_bread:10.2f}')

print('-' * 37)
print(f'Total Cost {total_bill:24.2f}')
