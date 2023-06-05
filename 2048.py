import functionality as game
    
def main():
    grid = game.createGrid()
    status = True
    
    while (status):
        game.currGrid(grid)
        commands = input("Enter one of the commands: ")
        
        for command in commands:
            if (command == "q"):
                status = False
            elif (command == "w"):
                grid = game.up(grid) 
            elif (command == "s"):
                grid = game.down(grid)
            elif (command == "a"):
                grid = game.left(grid)
            elif (command == "d"):
                grid = game.right(grid)
            else:
                print("ERROR: Invalid command")
            
        status = status and game.gameStatus(grid)
    
    game.currGrid(grid)
    print("GAMEOVER :(")
            
    
if (__name__ == "__main__"):
    main()