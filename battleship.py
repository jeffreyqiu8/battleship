def print_board(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(f"{grid[row][col]}", end="")
        print("")
def guess(grid, guess):
    if grid[guess[0]][guess[1]] == 'C':
        print("Carrier Hit!")
        grid[guess[0]][guess[1]] = 'c'
    elif grid[guess[0]][guess[1]] == 'B':
        print("Battleship Hit!")
        grid[guess[0]][guess[1]] = 'b'
    elif grid[guess[0]][guess[1]] == 'D':
        print("Destroyer Hit!")
        grid[guess[0]][guess[1]] = 'd'
    elif grid[guess[0]][guess[1]] == 'S':
        print("Submarine Hit!")
        grid[guess[0]][guess[1]] = 's'
    elif grid[guess[0]][guess[1]] == 'P':
        print("Patrol Boat Hit!")
        grid[guess[0]][guess[1]] = 'p'
    elif grid[guess[0]][guess[1]] == '.':
        print("Miss!")
        grid[guess[0]][guess[1]] = 'x'
def ship_locations(grid, ship):
    new = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == ship:
                new.append([row, col])
    return new
def game_over(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'P' or grid[row][col] == 'S' or grid[row][col] == 'C' or grid[row][col] == 'D' or grid[row][col] == 'B':
                return False
    return True
def add_ship(grid, ship, location, vertical = False):
    new = grid[:]
    length = 0
    if ship.lower() == "carrier":
        length = 5
    elif ship.lower() == "battleship":
        length = 4
    elif ship.lower() == "destroyer":
        length = 3
    elif ship.lower() == "submarine":
        length = 3
    elif ship.lower() == "patrol boat":
        length = 2
    else:
        print("Not a ship!")
        return grid
    letter = ship[0].upper()
    #check possibility
    if vertical and ((location[1] + length) > 9):
        print("Cannot Place!")
        return grid
    elif not vertical and ((location[0] + length) > 9):
        print("Cannot Place!")
        return grid
    # place ship
    if not vertical:
        for col in range(location[1], location[0] + length):
            if new[location[0]][col] == '.':
                new[location[0]][col] = letter
            else:
                print("Cannot Place!")
                return grid
    else:
        for row in range(location[0], location[0] + length):
            if new[row][location[1]] == '.':
                new[row][location[1]] = letter
            else:
                print("Cannot Place!")
                return grid
    return new
def print_board_hidden(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not(grid[row][col] == 'x' or grid[row][col] == 'p' or grid[row][col] == 'c' or grid[row][col] == 'd' or grid[row][col] == 'b' or grid[row][col] == 's'):
                print(".", end="")
            else:
                print(f"{grid[row][col]}", end="")
        print("")
    
game = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'S'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'S'],
    ['P', 'P', 'C', '.', '.', '.', '.', '.', '.', 'S'],
    ['.', '.', 'C', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'C', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'C', 'D', 'D', 'D', '.', '.', '.', '.'],
    ['.', '.', 'C', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'B', 'B', 'B', 'B', '.']
    ]
lostgame = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 's'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 's'],
    ['p', 'p', 'c', '.', '.', '.', '.', '.', '.', 's'],
    ['.', '.', 'c', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'c', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'c', 'd', 'd', 'd', '.', '.', '.', '.'],
    ['.', '.', 'c', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'b', 'b', 'b', 'b', '.']
    ]
emptygame = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]
print_board(game)
print(ship_locations(game, 'S'))
guess(game, [0, 8])
print_board(game)
print(ship_locations(game, 'S'))
print_board_hidden(game)
print(game_over(lostgame))
print_board(add_ship(emptygame, "Battleship", [0,0]))
