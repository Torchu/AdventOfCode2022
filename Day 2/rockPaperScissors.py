def calculate_points(oponent_choice: str, user_choice: str) -> int :
    """
    Calculates the points for the rock, paper, scissors game.
    :param oponent_choice: The choice of the oponent.
        - A for Rock.
        - B for Paper.
        - C for Scissors.
    :param user_choice: The choice of the user.
        - X for Rock.
        - Y for Paper.
        - Z for Scissors.
    :return: The points for the user.
    """
    POINT_MAP = {
        'A': {'X': 4, 'Y': 8, 'Z': 3},
        'B': {'X': 1, 'Y': 5, 'Z': 9},
        'C': {'X': 7, 'Y': 2, 'Z': 6}
    }
    return POINT_MAP[oponent_choice][user_choice]

def calculate_move(oponent_choice: str, result: str) -> str :
    """
    Calculates the points for the rock, paper, scissors game.
    :param oponent_choice: The choice of the oponent.
        - A for Rock.
        - B for Paper.
        - C for Scissors.
    :param result: The expected result of the round.
        - X for loss.
        - Y for draw.
        - Z for win.
    :return: The move that the user should make to get the expected result.
    """
    MOVE_MAP = {
        'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
        'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
        'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
    }
    return MOVE_MAP[oponent_choice][result]

print("Part I")
# Reads the input
stream = open("Day 2/input.txt", "r")
eof = False
total_points = 0
while(not eof):
    line = stream.readline()
    # Exit if we reach the end of the file
    if line == "":
        eof = True
    else:
        # Calculate the points
        total_points += calculate_points(line[0], line[2])
    
print(total_points)
            
print("Part II")
# Reads the input
stream = open("Day 2/input.txt", "r")
eof = False
total_points = 0
while(not eof):
    line = stream.readline()
    # Exit if we reach the end of the file
    if line == "":
        eof = True
    else:
        # Calculate the points
        user_move = calculate_move(line[0], line[2])
        total_points += calculate_points(line[0], user_move)
    
print(total_points)
