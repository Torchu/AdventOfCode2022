def get_rucksack(items: str) -> list[str]:
    """
    Divides the list of items of the rucksack into the two compartments.
    :param items: The list of items of the rucksack.
    :return: The list of items in each compartment. 
    """
    rucksack = []
    compartment_length = len(items) // 2
    rucksack.append(items[:compartment_length])
    rucksack.append(items[compartment_length:])
    return rucksack

def get_shared_item(rucksack: list[str]) -> str:
    """
    Gets the only item that is shared between the two compartments.
    :param rucksack: The list of items in each compartment.
    :return: The item that is shared between the two compartments.
    """
    return list(set(rucksack[0]) & set(rucksack[1]))[0]
        
def calculate_priority(item: str) -> int:
    """
    Calculates the priority of an item
    :param item: The item to calculate the priority. Valid items are [A,Z] and [a,z].
    :return: The priority of the item.
    """
    ascii_value = ord(item)
    if ascii_value >= 65 and ascii_value <=  90:
        # Capital letters priority is [27, 52]
        return ascii_value - 38
    elif ascii_value >= 97 and ascii_value <= 122:
        # Lower case letters priority is [1, 26]
        return ascii_value - 96
    else:
        raise Exception("Invalid item")

print("Part I")
# Reads the input
stream = open("Day 3/input.txt", "r")
eof = False
total_priority = 0
while(not eof):
    line = stream.readline()
    # Exit if we reach the end of the file
    if line == "":
        eof = True
    else:
        rucksack = get_rucksack(line)
        shared_item = get_shared_item(rucksack)
        total_priority += calculate_priority(shared_item)
        
print(total_priority)
