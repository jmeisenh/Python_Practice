

# a 2d list is a list of lists

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
# list has 4 rows and 3 columns
# print out he one

print(number_grid[0][0])
# double index is row then column or index number of list, and then element of that list
# number_grid[1][2] = 6

for row in number_grid:
    for col in row:
        print(col)

