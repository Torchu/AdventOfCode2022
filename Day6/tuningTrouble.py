def isMarker(marker: str, length: int) -> bool:
    """
    Checks if a marker is valid.
    :param marker: The marker to check.
    :param length: The length of the marker.
    :return: True if the marker is a string on non repeated characters.
    """
    if len(marker) != length:
        return False
    for i in marker:
        if marker.count(i) > 1:
            return False
    return True

def getMarker(buffer: str, length: int) -> int:
    """
    A marker is the first of a certain length characters that are not repeated in the buffer.
    Gets the position of the marker in the buffer.
    :param buffer: The buffer to get the marker from.
    :param length: The length of the marker.
    :return: The position of the marker in the buffer, starting from 1.
    """
    for i in range(0, len(buffer)-length):
        marker = buffer[i:i+length]
        if isMarker(marker, length):
            return i+length

# Gets the buffer
stream = open("Day6/input.txt", "r")
buffer = stream.read()
print("Package markers", getMarker(buffer, 4))
print("Message markers", getMarker(buffer, 14))
