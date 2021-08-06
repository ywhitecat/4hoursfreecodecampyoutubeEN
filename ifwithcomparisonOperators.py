a=float(input("1st number: ")) 
b=float(input("2nd number: "))
c=float(input("3nd number: "))

#the elif executes if the previous conditions were not true

#a = 33
#b = 33
#if b > a:
# print("b is greater than a")
#elif a == b:
#  print("a and b are equal")

#seach for the comparison operator at https://www.w3schools.com/python/python_operators.asp

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("The maximum number of the sequence is " + str(max_num(a,b,c)))