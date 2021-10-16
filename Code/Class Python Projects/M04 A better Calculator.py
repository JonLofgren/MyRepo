carry = 0
flag = False  # Lets the logic know if there was a previous calculation

def calculate(x, y, op):  # Returns the value of the selected opperation
    global flag
    if op == 1:
        return (x + y)
    elif op == 2:
        return (x - y)
    elif op == 3:
        return (x * y)
    elif op == 4:
        if y == 0:  # Checks if dividing by zero
            print("You can not divide by zero!")
            flag = False
        else:
            return (x / y)


def input_values(reuse=False):
    global flag  #   \
    global carry  #   > Sets these variables to be changed globally, not just in this function
    global num1  #   /
    while True:  # Prompts the user to input the needed information
        try:
            if not reuse:  # Takes out the first input if the user wants to use the previous output as the first input
                num1 = int(input("Choose the first number\n"))
            num2 = int(input("Choose the second number\n"))
            while True:
                try:
                    operation = int(input("Add - 1\nSubtract - 2\nMultiply - 3\nDivide - 4\n"))
                    if operation == 1 or operation == 2 or operation == 3 or operation == 4:
                        output = calculate(num1, num2, operation)
                        if output == None:  # Checks if the calculation divided by zero
                            carry = 0
                            break
                        else:
                            print(f"The result of the calculation is: {output}.")  # Outputs and sets the Flag
                            carry = output
                            flag = True
                        break
                except ValueError:
                    print("Please input a valid choice!\n")
            break
        except ValueError:
            print("Pick a valid number\n")
            continue


  # Selection for if user wants to use the calculator

while True:
    choice1 = input("Do you want to use the better calculator? Y|n\n").lower()
    if choice1 == "y" or choice1 == "":
        if flag:  # checks if there was a previous calculation by checking if the flag is set
            while True:
                choice2 = input(f"Would you like to use {carry} as your first input? Y|n\n").lower()  # Determines if the user wants to use the output from previous calculation as the input for the next
                if choice2 == "y" or choice2 == "":
                    num1 = carry
                    input_values(True)  # True implies that the first input is the carry from last calculation
                    break
                elif choice2 == "n":
                    input_values()
                    break
                else:
                    print("Please input a valid choice!\n")  # If an error occurs, notify the user
        else:
            input_values()
    elif choice1 == "n":
        print("Exiting")  # Breaks the program out of the loop
        break
    else:
        print("Please input a valid choice!\n")  # If an error occurs, notify the user