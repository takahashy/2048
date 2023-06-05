'''
2048.py
2022, August 1

Creating the 2048 game for user to play
'''

from random import randint

# create a 4 x 4 grid with 0s
def createGrid():
    grid = []

    for i in range(4):
        grid.append([0] * 4)
    
    print("\nPlay 2048!")
    print("To move the numbers enter the following:\n", 
          "\'w\': Move up\n",
          "\'s\': Move down\n",
          "\'a\': Move left\n",
          "\'d\': Move right\n",
          "\'q\': QUIT\n", sep = "")
    
    generate2(grid)
    return grid

# Print current state of the grid
def currGrid(grid):
    one_digit   = True
    two_digit   = False
    three_digit = False
    four_digit  = False 
    
    for j in grid:
        for cell in j:
            if (cell >= 1000):
                four_digit  = True
            elif (cell >= 100):
                three_digit = True
            elif (cell >= 10):
                two_digit = True            

    if (four_digit):
        three_digit = False
        two_digit   = False
        one_digit   = False
        printFour(grid)        
        
    if (three_digit):
        two_digit = False
        one_digit = False
        printThree(grid) 
            
    if (two_digit):
        one_digit = False
        printTwo(grid)
        
    if (one_digit):
        printOne(grid)     
        
def printFour(grid):
    for i in range(4):
        print("[", end = "")
        for j in range(4):
            if (j == 3):
                print(grid[i][j], end = "")
            else:
                if (grid[i][j] >= 1000):
                    print(grid[i][j], end = " ")
                elif (grid[i][j] >= 100):
                    print(grid[i][j], end = "  ")
                elif (grid[i][j] >= 10):
                    print(grid[i][j], end = "   ") 
                else:
                    print(grid[i][j], end = "    ")         
        print("]")    
        
def printThree(grid):
    for i in range(4):
        print("[", end = "")
        for j in range(4):
            if (j == 3):
                print(grid[i][j], end = "")
            else:
                if (grid[i][j] >= 100):
                    print(grid[i][j], end = " ")
                elif (grid[i][j] >= 10):
                    print(grid[i][j], end = "  ") 
                else:
                    print(grid[i][j], end = "   ")         
        print("]") 
     
def printTwo(grid):
    for i in range(4):
        print("[", end = "")
        for j in range(4):
            if (j == 3):
                print(grid[i][j], end = "")
            else:
                if (grid[i][j] >= 10):
                    print(grid[i][j], end = " ")
                else:
                    print(grid[i][j], end = "  ")  
        print("]")  
     
def printOne(grid):
    for i in range(4):
        print("[", end = "")
        for j in range(4):
            if (j == 3):
                print(grid[i][j], end = "")
            else:
                print(grid[i][j], end = " ")  
        print("]") 
     
# Check if game lost
def gameStatus(grid):
    won = False
    for i in grid:
        for j in i:
            if (j == 2048):
                print("\n\nCONGRATULATIONS YOU GOT 2048!")
                return True
            
            if (j == 0):
                won = True
    
    for i in range(3):
        for j in range(3):
            if (grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i][j + 1]):
                return True
        
    for i in range(3):
        if (grid[i][3] == grid[i + 1][3]):
            return True
    
    for j in range(3):
        if (grid[3][j] == grid[3][j + 1]):
            return True
            
    return won

# Generates a 2 in any open position
def generate2(grid):
    row = randint(0, 3)
    col = randint(0, 3)

    while (grid[row][col] != 0):
        row = randint(0, 3)
        col = randint(0, 3)
 
    grid[row][col] = 2
    
# reflect the grid b the horizontal middle
def reflect(grid):
    new_grid = []
    
    for i in range(4):
        new_grid.append(grid[3 - i])
        
    return new_grid

# transpose the matrix
def tranpose(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([0] * 4)
    
    for i in range(4):
        for j in range(4):
            new_grid[j][i] = grid[i][j]
            
    return new_grid

# moving all the numbers up
def move(grid):
    new_grid = []
    changes = False
    for i in range(4):
        new_grid.append([0] * 4)
        
    for col in range(4):
        up = 0
        for row in range(4):
            if (grid[row][col] != 0):
                new_grid[up][col] = grid[row][col]
                
                if (up != row):
                    changes = True
                up += 1
                
    return new_grid, changes

# if the number right below is the same double the value
def merge(new_grid):
    changes = False
    for i in range(3):
        for j in range(4):
            if ((new_grid[i][j] == new_grid[i + 1][j]) and (new_grid[i][j] != 0)):
                new_grid[i][j] *= 2
                new_grid[i + 1][j] = 0
                changes = True
    return changes
         
# Function when user enters up       
def up(grid):
    new_grid, change_move = move(grid)
    change_merge = merge(new_grid)    
    new_grid, change_move1 = move(new_grid)
    
    # can only generate a 2 if something has changed
    if (change_move or change_merge):    
        generate2(new_grid)
    
    return new_grid

# Function when user enters down
def down(grid):
    new_grid, change_move = move(reflect(grid))
    change_merge = merge(new_grid)
    new_grid, change_move1 = move(new_grid)
    
    if (change_move or change_merge):    
        generate2(new_grid)

    return reflect(new_grid)

# Function when user enters left
def left(grid):
    new_grid, change_move = move(tranpose(grid))
    change_merge = merge(new_grid)
    new_grid, change_move1 = move(new_grid)
    
    if (change_move or change_merge):    
        generate2(new_grid)

    return tranpose(new_grid)

# Function when user enters right
def right(grid):
    new_grid, change_move = move(reflect((tranpose(grid))))
    change_merge = merge(new_grid)
    new_grid, change_move1 = move(new_grid)
    
    if (change_move or change_merge):    
        generate2(new_grid)

    return tranpose(reflect(new_grid))
          
# # move all the numbers in the grid down
# def moveAllDown(grid):
#     new_grid = []
#     for i in range(4):
#         new_grid.append([0] * 4)
        
#     for col in range(4):
#         down = 3
#         for row in range(4):
#             if (grid[3 - row][col] != 0):
#                 new_grid[down][col] = grid[3 - row][col]
#                 down -= 1
                
#     return new_grid

# def moveLeft(grid):

# def moveRight(grid):


                
# def mergeDown(new_grid):
#     for i in range(3):
#         for j in range(4):
#             if ((new_grid[3 - i][j] == new_grid[2 - i][j]) and (new_grid[3 - i][j] != 0)):
#                 new_grid[3 - i][j] *= 2
#                 new_grid[2 - i][j] = 0

# input by the user should be
#   .a - left
#   .s - down
#   .d - right
#   .w - up
#   .q - quit

# lose the program when all the positions are filled with numbers and cannot merge any numbers(less than 2048)

