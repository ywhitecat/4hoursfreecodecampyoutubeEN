import time
#I wake up
#If i'm hungry, I eat breakfast

#I leave my house, if its cloudy
#I bring an umbrella, otherwise i bring sunglasses

#Im at the restaurant, If I want meat
# I order a steak otherwise if i want pasta
# I order spaghetti & meatballs otherwise i order a salad
def main():
    return time.sleep(1)


height = input("Type your height cm: ")
gender = input("type your gender male/female: ")

if height > str(170):
    height=1
else:
    height=0

if gender == str("male"):
    gender=1
else:
    gender= str("famale")
    gender = 0


is_male = gender             # test change to false/true 1/0 boolean statement
is_tall = height


if is_male and is_tall:
    print("You are a tall male")

elif is_male and not(is_tall):
    print("you're a short male")

elif not(is_male) and is_tall:
    print("you're a tall female")

else:
    print("You are not a tall female")

main()