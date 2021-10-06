# Area and perimeter calculator
# Author: Corey Lynch
# Date: 27/09/2019

user_length = int(input('Enter the length of the rectangle.'))
user_width = int(input('Enter the width of the rectangle.'))

area = user_length * user_width
perimeter = user_length * 2 + user_width * 2

print('The area of the rectangle is', area, 'cm sq and the perimeter',
                                            'is', perimeter, 'cm')
