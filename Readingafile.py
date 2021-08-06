#fileforRead = open("fileforRead.txt","r") #r to Read, W to Write, a to append()add new info, r+ reading and writing
list1 = open("fileforRead.txt","r+") #r to Read, W to Write, a to append
#fileforRead.readable() to check if the file is readable
#print(fileforRead.readline()[0:])
print(list1.readlines()[0:])

#list1.append('something')
'''
Reading/Writing files part: 03:12:00
https://www.youtube.com/watch?v=rfscVS0vtbw&t=10362s&ab_channel=freeCodeCamp.org


'''


list1.close()