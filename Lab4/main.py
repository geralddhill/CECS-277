# Names: Gerald Hill, Hoang Do
# Date: 9/16/24
# Desc: Plays treasure hunt game with user


def read_map():
    ''' Reads the map from a file ("map.txt")

    Args: None

    Returns: A 2D array representing the map
    '''
    file = open("map.txt")
    map = []
    for row in file:
        map_row = []
        for point in row:
            if point != '\n' and point != ' ':
                map_row.append(point)
        map.append(map_row)

    file.close()
    return map



def display_map(map, player):
    ''' Displays the map with the player on it

    Args:
        - map: the map as a 2D array
        - player: the player coordinates as a list

    Return: Nothing is returned. Map is printed to screen
    '''
    for x, row in enumerate(map):
        for y, point in enumerate(row):
            # Checks if player is on that space
            if player[0] == x and player[1] == y:
                print("P",end='')
            else:
                print(point,end='')
            print(' ',end='')
        print()



def move_player(player, dir, upper_bound):
    ''' Takes in a direction and moves the player if possible

    Args:
        - player: the player coordinates as a list
        - dir: the direction the player wants to move (as WASD)
        - upper_bound: the max coordinate on both dimensions that the player can move

    Returns: New player location
    '''
    # Initializes new player location to update
    player_new = player
    # Up
    if dir == 'W':
        if player_new[0] <= 0:
            print("Player cannot move out of bounds.")
        else:
            player_new[0] -= 1
    # Left
    elif dir == 'A':
        if player_new[1] <= 0:
            print("Player cannot move out of bounds.")
        else:
            player_new[1] -= 1
    # Down
    elif dir == 'S':
        if player_new[0] >= (upper_bound - 1):
            print("Player cannot move out of bounds.")
        else:
            player_new[0] += 1
    # Right
    elif dir == 'D':
        if player_new[1] >= (upper_bound - 1):
            print("Player cannot move out of bounds.")
        else:
            player_new[1] += 1
    # This should never occur
    else:
        print("Error in direction input.")

    # Returns new player location
    return player_new



def count_treasures_traps(map, player, upper_bound):
    ''' Counts the number of treasurs and traps around the player

    Args:
        - map: the map as a 2D list
        - player: the player's location as a list
        - upper_bound: the max coordinate on both dimensions that the player can move

    Returns: Returns the number of treasures and traps as ints (in that order)
    '''
    # Initializes count variables
    treasures = 0
    traps = 0

    # Finds which range to search and makes sure it's not past the upper bound
    search_range = [list(range((player[0] - 1), (player[0] + 2))), list(range((player[1] - 1), (player[1] + 2)))]
    if search_range[0][2] > upper_bound - 1:
        search_range[0].pop(2)
    if search_range[0][0] < 0:
        search_range[0].pop(0)
    if search_range[1][2] > upper_bound - 1:
        search_range[1].pop(2)
    if search_range[1][0] < 0:
        search_range[1].pop(0)

    # Searches the map
    for x in search_range[1]:
        for y in search_range[0]:
            if x == player[1] and y == player[0]:
                continue

            if map[y][x] == 'T':
                treasures += 1
            elif map[y][x] == 'X':
                traps += 1

    return treasures, traps



def main():
    ''' Plays treasure hunt game with user '''
    player_map = [['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.']]
    solution_map = read_map()
    player = [0, 0]
    upper_bound = 7
    letter = ['W','A','S','D','L','Q']
    dir = ''
    treasures_found = 0
    treasures_left = 7

    print("Treasure hunt!")
    print("Find the", treasures_left ,"treasures without getting caught in trap. Look around to spot")
    print("nearby traps and treasures")
    while dir != 'Q':
        # Displays map and asks for input
        display_map(player_map, player)
        dir = input("Enter direction (WASD or L to look around or Q to quit) ").upper()
        if dir not in letter:
            print("Invalid input")
        # Early exit if quit
        elif dir == 'Q':
            continue
        # Updates map if player looks around
        elif dir == 'L':
            treasures, traps = count_treasures_traps(solution_map, player, upper_bound)
            if player_map[player[0]][player[1]] != 'T':
                player_map[player[0]][player[1]] = traps
            print ("You detect", treasures, "treasures nearby.")
            print ("You detect", traps, "traps nearby.")
        else:
            player = move_player(player, dir, upper_bound)
            # Tests if player found a trap (early return)
            if solution_map[player[0]][player[1]] == 'X':
                print("You were caught in a trap!")
                print("You found", treasures_found, "treasures.")
                display_map(player_map, player)
                print("Game Over!")
                return
            #Tests if player found a treasure
            if solution_map[player[0]][player[1]] == 'T':
                player_map[player[0]][player[1]] = 'T'
                treasures_left -= 1
                treasures_found += 1
                # Early return if all treasures are found
                if treasures_left == 0:
                    print("You found all the treasures!")
                    display_map(player_map, player)
                    print("Thanks for playing!")
                    return
                print("You found treasure!")
                print("There are", treasures_left, "treasures remaining.")




main()