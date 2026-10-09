try:
    x = int(input("Please enter a number."))
    print("Your age is", x)
except ValueError as ex:
    print("The error is", ex)
    print("You have not entered a number. Please enter something more valid.")