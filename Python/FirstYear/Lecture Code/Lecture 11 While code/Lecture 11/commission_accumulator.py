# This program calculates sales commissions.
# Create a variable to control the loop.
keep_going = 'y'

total_commission = 0.0

# Calculate a series of commissions.
while keep_going == 'y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the commission.
    commission = sales * comm_rate / 100

    # Add the current commission to the running total
    total_commission += commission

    # Display the commission.
    print('The commission is €{:.2f}'.format(commission))

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate '
                       'another commission (Enter y for yes): ')

print("Your total commission is €{:.2f}".format(total_commission))