#tuple is very similar to a list, a structure to store information, but with a difference
# tuple is immutable, you cannot change it, add or remove elements
#a tuple is a permanent list
coordinates = (4,5)
 # index positon 0,1
print(coordinates[0:])
name = input("enter your name ")
age = input("enter your age ")

#fUNCTIONS

        #you can add some paramenter inside of the function
def say_hi(name, age):    # give a function a name, :(colon) means all the code after this sign its going to the inside of the function
    #inside of the funtion space
    print("Hello " + name)
    print("you're " + age + " years old")


#outside of the function space

def cube(num):
    return num*num*num



#now we have to call it
#print("top")
say_hi(name,age)
#print("bottom")
print(cube(3))

