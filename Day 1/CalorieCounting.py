# Generates a the list of calories of each elf
stream = open("Day 1/CalorieCountingInput.txt", "r")
eof = False
calories = 0
max_calories = 0
while(not eof):
    line = stream.readline()
    # Exit if we reach the end of the file
    if line == "":
        eof = True
    # Resets the counter if we reach an empty line
    elif line == "\n":
        calories = 0
    # Add the calories to the counter and check for the record
    else:
        calories += int(line)
        if calories > max_calories:
            max_calories = calories
            
print(max_calories)
