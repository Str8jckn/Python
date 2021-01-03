# imports
from menu import print_menu, print_header, clear, print_line, print_product
from product import Product

#global vars
catalog = []
next_id = 1
# functions


def register_product():
    global next_id
    try:
        print_header("Register a new Product")
        title = input('plz provide the title:')
        category = input('plz provide the category:')
        stock = int(input('plz provide stock number:'))
        price = float(input('plz provide the $$$: '))

        the_product = Product(next_id, title, category, stock, price)
        next_id = next_id + 1

        catalog.append(the_product)

    except:
        print_line()
        print("** PRoduct Registered **")


def print_catalog():
    print_header("Current Catalog")

    for prod in catalog:
        print_product(prod)


def print_out_of_stock():
    print_header("Out of Stock")

    for prod in catalog:
        if(prod.stock == 0):
            print_product(prod)


def total_stock():
    print_header("Total stock value")

    total = 0.0
    for prod in catalog:
        total = total + (prod.stock * prod.price)

    print(str(total))


def cheap_stock():
    print_header("Cheapest product")

    prices = []
    for prod in catalog:
        prices.append(prod.price)

    cheapest = min(prices)
    print("The cheapest is" + str(cheapest))


def cheapest_product_adv():
    print_header("Cheapest product adv")

    if(len(catalog) < 1):
        print("** Error, empty catalog.")
        return

    cheapest = catalog[0]
    for prod in catalog:
        if(prod.price < cheapest.price):
            cheapest = prod

    print_product(cheapest)


def delete_product():
    print_header("Delete a product")

    print_catalog()
    id = input("Please select id to delete: ")
    found = False
    for prod in catalog:
        if(str(prod.id) == id):
            found = True
            catalog.remove(prod)
    if(found):
        print("Product Removed!")
    else:
        print("***Err***")
        return


def update_price():
    print_header("Update prod price")

    print_catalog()
    select = input("Please select product price you'd like to update: ")
    found = False
    for prod in catalog:
        if(str(prod.id) == select):
            found = True
            new_price = float(input("enter new price: "))
            prod.price = new_price

    if(found):
        print("Price for " + str(prod.title) + "has been updated")
    else:
        print("***Err***")


def update_stock():
    print_header("Update prod stock")

    print_catalog()
    select = input("Please select product id you'd like to update: ")
    found = False
    for prod in catalog:
        if(str(prod.id) == select):
            found = True
            new_stock = int(input("enter new price: "))
            prod.stock = new_stock

    if(found):
        print("Price for " + str(prod.title) + "has been updated")
    else:
        print("***Err***")


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
    cheapest_product_adv()

elif(opt == '6'):
    delete_product()

elif(opt == '7'):
    update_price()

elif(opt == '8'):
    update_stock()

# elif(opt == 'a'):
 #   calculate_age()

# elif(opt == 'b'):
#    calculate_tip()

input("Press Enter to continue...")

print("Good day!")
