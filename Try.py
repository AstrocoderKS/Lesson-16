try:
    x = int(input("Please enter a number."))
    print("The number you have entered is", x)
except ValueError as ex:
    print("The error is", ex)
    print("You have not entered a number.")