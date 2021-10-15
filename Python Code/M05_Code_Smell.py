def is_num(question):
    while True:
        try:
            x = float(input(question))
            return x
        except ValueError:
            print("\nThat is not a number.\n")
            continue
    return x

shopping_cart = []
response = "y"
total = 0

while response != "n":
    shopping_cart.append(is_num("Enter the price of your item: $"))
    response = input("Add more items to your cart? Y|n: ").lower()
    while True:
        if response == "y" or response == "":
            break
        elif response == "n":
            break
        else:
            response = input("\nPlease enter a 'Y' for yes or a 'N' for no: ").lower()
        break
if len(shopping_cart) < 11:
    total = sum(shopping_cart)
elif len(shopping_cart) > 24:
    total = sum(shopping_cart) * 0.75
elif len(shopping_cart) > 11:
    total = sum(shopping_cart) * 0.85
tax = total * 1.08
print(f"The total is: ${tax:.{2}f}.")
