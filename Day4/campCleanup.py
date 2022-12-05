from typing import Tuple


def getRanges(line: str) -> Tuple[int, int, int, int]:
    """
    Gets the ranges from a line of input
    :param line: The line of input
    :return: The ranges as 4 integers. First the range of the first elf of the pair, and then the range of the second one
    """
    elves = line.split(",")
    elf1 = elves[0].split("-")
    elf2 = elves[1].split("-")
    return int(elf1[0]), int(elf1[1]), int(elf2[0]), int(elf2[1])

def isContaining(leftRange1: int, rightRange1: int, leftRange2: int, rightRange2: int) -> bool:
    """
    Checks if the one range is containing the other
    :param leftRange1: The left side of the first range
    :param rightRange1: The right side of the first range
    :param leftRange2: The left side of the second range
    :param rightRange2: The right side of the second range
    :return: True if one range is containing the other one, False otherwise
    """
    return (leftRange1 <= leftRange2 and rightRange1 >= rightRange2) or (leftRange2 <= leftRange1 and rightRange2 >= rightRange1)

def isOverlaping(leftRange1: int, rightRange1: int, leftRange2: int, rightRange2: int) -> bool:
    """
    Checks if the two ranges are overlapping
    :param leftRange1: The left side of the first range
    :param rightRange1: The right side of the first range
    :param leftRange2: The left side of the second range
    :param rightRange2: The right side of the second range
    :return: True if the two ranges are overlapping, False otherwise
    """
    return leftRange1 <= leftRange2 <= rightRange1 or leftRange1 <= rightRange2 <= rightRange1 or leftRange2 <= leftRange1 <= rightRange2 or leftRange2 <= rightRange1 <= rightRange2


print("Part I")
# Reads the input
stream = open("Day4/input.txt", "r")
eof = False
result = 0
while(not eof):
    line = stream.readline()
    # Exit if we reach the end of the file
    if line == "":
        eof = True
    else:
        l1, r1, l2, r2 = getRanges(line)
        if isContaining(l1, r1, l2, r2):
            result += 1
            
print(result)
        

print("Part II")
# Reads the input
stream = open("Day4/input.txt", "r")
eof = False
result = 0
while(not eof):
    line = stream.readline()
    # Exit if we reach the end of the file
    if line == "":
        eof = True
    else:
        l1, r1, l2, r2 = getRanges(line)
        if isOverlaping(l1, r1, l2, r2):
            result += 1
            
print(result)
