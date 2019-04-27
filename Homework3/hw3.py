# Your name and email here
# Markus Tran
# mkhtran@ucdavis.edu

from Node import Node

# Problem 1

def findSmallest(items):
    length = len(items)

    # Base cases
    if (length == 0):
        return None
    if (length == 1):
        return items[0]

    # Recursive step
    first = items[0]
    nextSmallest = findSmallest(items[1:])
    return first if first <= nextSmallest else nextSmallest

# Problem 2

def findValue(value, linkedList):
    # Base case
    if linkedList == None:
        return False

    # Recursive step
    return linkedList.getData() == value or findValue(value, linkedList.getNext())

# Problems 3 and 5

def ladder(rungs, knownResults = {}):
    # Check cache
    if rungs in knownResults:
        return knownResults[rungs]
    result = None

    # Solutions fall into 2 categories
    # - Starts with 1 followed by a solution for (n - 1)
    # - Starts with 2 followed by a solution for (n - 2)
    #
    # Let S(n) be the number of solutions for a given n. Thus S follows the
    # recurrence relation:
    #   S(n) = S(n-1) + S(n-2)

    # Base cases
    # This assumes there is exactly 1 way to climb a ladder with 0 rungs.
    # That way S(n) corresponds to F(n+1) where F(n) is the nth Fibonacci number.
    if rungs <= 1:
        result = 1

    # Recursive step
    else:
        result = ladder(rungs - 1) + ladder(rungs - 2)

    knownResults[rungs] = result
    return result

# Problem 4

def recPal(str):
    # Base case
    # This assumes that the empty string is vacuously a palindrome.
    if str == '':
        return True

    # Recursive step
    return str[0] == str[-1] and recPal(str[1:-1])
