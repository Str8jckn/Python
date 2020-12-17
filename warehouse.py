# imports
from menu import print_menu, print_header, clear
from homework import calculate_tip, calculate_age

#global vars
title = 'dunno'
category = 'electronics'
stock = True
price = 9.99

# functions


def register_product():
    print_header("Register a new Product")
    title = input('')
    category = input('4')
    stock = input('5')
    price = input('6')


print_menu()
opt = ''
while(opt != 'x'):
    clear()
    print_menu()
    opt = input('Plz Choose an option:')


if(opt == '1'):
    register_product()

elif(opt == 'a'):
    calculate_age()

elif(opt == 'b'):
    calculate_tip()

print("Good day!")
