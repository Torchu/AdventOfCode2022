print("Part I")
crates = []
stream = open("Day5/input.txt", "r")
lines = stream.readlines()

# Gets the number of crates
n_crates = int([line for line in lines if "1" in line][0].strip()[-1])
for i in range(n_crates):
    crates.append([])

# Gets the initial cargo of the crates
for line in filter(lambda x: "[" in x, lines):
    for i in range(0, int(len(line)/4)):
        if line[4*i] == "[":
            crates[i].insert(0, line[4*i+1])
            
# Gets the commands
for line in filter(lambda x: "move" in x, lines):
    line_data = line.split(" ")
    cargo_to_move = int(line_data[1])
    crate_from = int(line_data[3])-1
    crate_to = int(line_data[5])-1
    for i in range(cargo_to_move):
        crates[crate_to].append(crates[crate_from].pop())

# Prints the superior cargo of each crate
result = ""
for i in range(n_crates):
    result += crates[i][-1]
print(result)

print("Part II")
crates = []
stream = open("Day5/input.txt", "r")
lines = stream.readlines()

# Gets the number of crates
n_crates = int([line for line in lines if "1" in line][0].strip()[-1])
for i in range(n_crates):
    crates.append([])

# Gets the initial cargo of the crates
for line in filter(lambda x: "[" in x, lines):
    for i in range(0, int(len(line)/4)):
        if line[4*i] == "[":
            crates[i].insert(0, line[4*i+1])
            
# Gets the commands
for line in filter(lambda x: "move" in x, lines):
    line_data = line.split(" ")
    cargo_to_move = int(line_data[1])
    crate_from = int(line_data[3])-1
    crate_to = int(line_data[5])-1
    last_cargo_idx = len(crates[crate_to])
    for i in range(cargo_to_move):
        crates[crate_to].insert(last_cargo_idx, crates[crate_from].pop())

# Prints the superior cargo of each crate
result = ""
for i in range(n_crates):
    result += crates[i][-1]
print(result)
