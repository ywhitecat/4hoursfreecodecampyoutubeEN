number_grid = [
    [1,2,3], #row 0 
    [4,5,6], #row 1
    [7,8,9], #row 2
    [0]      #row 3  
]

print(number_grid[0][1]) #prints out the element for 0/1 row number and collumn number
# in this case is 2

for row in number_grid:
    for col in row:
        print(col) #prints out all individual number in the list
