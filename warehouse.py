# imports
from menu import print_menu, print_header, clear, print_line, print_product
from homework import calculate_age, calculate_tip
from product import Product

#global vars
catalog = []

# functions


def register_product():
    print_header("Register a new Product")
    title = input('plz provide the title:')
    category = input('plz provide the category:')
    stock = int(input('plz provide stock number:'))
    price = float(input('plz provide the $$$'))


the_product = Product(0, title, category, stock, price)

catalog.append(the_product)


print_line()
print("** PRoduct Registered **")


def print_catalog():
    print_header("Current Catalog")

    for prod in catalog:
        print_product(prod)


def print_out_of_stock():
    print_header("Out of Stock")

    for print_out_of_stock in catalog:
        if(prod.stock == 0):
            print_product(prod)


def total_stock():
    print_header("Total Stock Value")

    total = 0.0
    for prod in catalog:
        total = total + (prod.stock * prod.price)

    print(str(total))


print_menu()
opt = ''
while(opt != 'x'):
    clear()
    print_menu()
    opt = input('Plz Choose an option:')


if(opt == '1'):
    register_product()

elif(opt == '2'):
    print_catalog()

elif(opt == '3'):
    print_out_of_stock()

elif(opt == '4'):
    total_stock()

elif(opt == '5'):
    cheap_stock()

elif(opt == 'a'):
    calculate_age()

elif(opt == 'b'):
    calculate_tip()

input("Press Enter to continue...")

print("Good day!")
