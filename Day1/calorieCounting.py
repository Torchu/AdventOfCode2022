print("Part I")

# Reads the input
stream = open("Day1/input.txt", "r")
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

print("Part II")

# Reads the input
stream = open("Day1/input.txt", "r")
eof = False
calories = 0
calories_by_elf = []
while(not eof):
    line = stream.readline()
    # Exit if we reach the end of the file
    if line == "":
        eof = True
    # Resets the counter and stores the calories if we reach an empty line
    elif line == "\n":
        calories_by_elf.append(calories)
        calories = 0
    # Add the calories to the counter
    else:
        calories += int(line)
        
# Sorts the list to get the top 3
calories_by_elf.sort(reverse=True)
            
print(calories_by_elf[0] + calories_by_elf[1] + calories_by_elf[2])
