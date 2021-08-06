character_name = "John" # you only need quotation mark to store a string
character_age= "50"
#boolean variable

is_Male = True

print("There was once a man named " + character_name +",")
print("He was " + character_age + " years old.")
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".\n\n\n")

#working with units (text)

print("Giraffe\n Academy")  #\n inserts a new line
print("Giraffe \"Academy\"") #if you wanna print out a quotation mark in the text
print("Giraffe\Academy")  #\ backslash
# also create a string variable

phrase="SOME RANDOM STUFF HERE"

print(phrase.lower() + " is printed in lower case\n\n".upper()) #its called concatenation, process of taking a string and appending another on it
#commands .lower() and .upper() for the word cases

#true or false statements
print(phrase.lower().isupper()) #is it true that's an upper case phrase?? in converted off coarse

#length function
print(len(phrase))

#grab a character in order with brackets []
print(phrase[0] + "") # the first always start with 0

#index function, where that specific letter is located
print(phrase.index("A")) # its gonna tell where it starts, an error might occur if it doesnt have the value

#replacement in a string
print(phrase.replace("SOME","Other"))

