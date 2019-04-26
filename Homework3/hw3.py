# Your name and email here
# Markus Tran
# mkhtran@ucdavis.edu

# Problem 1

def findSmallest(items):
    length = len(items)

    # Base cases
    if (length == 0):
        return None
    if (length == 1):
        return items[0]

    # Return the first element OR the smallest of the remaining elements
    first = items[0]
    nextSmallest = findSmallest(items[1:])
    return first if first <= nextSmallest else nextSmallest

# Problem 2

def findValue(value, linkedList):
    raise NotImplementedError

# Problems 3 and 5

def ladder(rungs):
    raise NotImplementedError

# Problem 4

def recPal(str):
    raise NotImplementedError
