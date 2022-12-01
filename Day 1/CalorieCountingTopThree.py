# Generates a the list of calories of each elf
stream = open("Day 1/CalorieCountingInput.txt", "r")
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
