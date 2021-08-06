

try:
    value =10/0
    number= int(input("Enter a number "))

    print(number)
except ZeroDivisionError: 
    print("You can't divide by 0")
except ValueError:
    print("invalid input")