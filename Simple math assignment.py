import time

input1 = int(input("Choose your first number:\n"))
input2 = int(input("Choose your second number:\n"))

add = input1 + input2
sub = input1 - input2
product = input1*input2
quotient = input1/input2

print("Calculating", end="")
for i in range(10):
    print(".", end="")
    time.sleep(.25)
print()

print(f"Sum: {add}; Difference: {sub}; Product: {product}; Quotient: {quotient}.")