#list used to deal with a large amount of data
#So, first give a name for the list
#[] to store bunch of different values
#you can put numbers, boolean, strings
friends = ["Andre","randomguy","someguy",2]
  #          0       1           2       3

friends[1]="Mike" #modifies the value in the lists 
print(friends[-1]) # if you use negative number, you can access to the back of the list

print(friends[1:2]) # specify a range to select, if you took out the 3, it will access the rest after the 1


#LISTS FUNCTIONS

lucky_numbers = [4,8,15,16,23,42]

friends.extend(lucky_numbers) #adds a list to another
friends.append('chris') #adds an item at the end of the list
friends.insert(1,"kelly") #adds at 1 index an element pushing the others to the right
friends.remove("kelly") 
friends.pop() # removes the last elements of the list
print(friends.index("Andre")) # points positions of the list
print(friends.count("Andre")) # counts how many Andre are in the list
lucky_numbers.sort() # to sort in other
lucky_numbers.reverse()# to reverse the order of items
print(friends)