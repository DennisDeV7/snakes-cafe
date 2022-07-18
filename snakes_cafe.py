print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

# initialize empty meal dictionary
meal = {}

# Start loop here until user enters quit
while True:

    # Create a variable to store the user order
    order = input("> ")
    print()

    # Gives the ability to break from the loop if you enter "quit"
    if order == 'quit':
        break

    # If the order is not in the dictionary it will add it with a base value of "1"
    # if it is already in the dict it will increment by 1.
    if order not in meal:
        meal[order] = 1
    else:
        meal[order] += 1

    # print the order
    if meal[order] == 1:
        report = f"** {meal[order]} order of {order} have been added to your meal **\n"
        print(report)
    if meal[order] > 1:
        report = f"** {meal[order]} orders of {order} have been added to your meal **\n"
        print(report)
# end loop

print("Here is a summary of your order:")
for order, qnt in meal.items():
    print(f"{order}: {qnt}")
