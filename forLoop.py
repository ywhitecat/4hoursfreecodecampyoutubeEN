#loop over different collection, specific purpose

for letter in "Giraffe Academy": # for each letter for the following string
    print(letter)    # print out each letter for the string


# for arrays


friends=["jim", "Karen", "Kevin"]
#for the fist term(friends, index) its whatever you want
for friends in friends:
    print(friends)

for index in range(10):
    print(index) # its gonna print out 0-9, counting the 0

for index in range(3,10): #3 to 10, not including 10
    print(index)

for index in range(len(friends)):
    print(friends[index])