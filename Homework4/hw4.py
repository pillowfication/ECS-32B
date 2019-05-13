# Your name and email here
# Markus Tran
# mkhtran@ucdavis.edu

# Problem 1

def sequentialSearchRec(alist, item, index=0):
    if alist[index] == item:
        return True  # OR return index
    if index == len(alist) - 1:
        return False # OR return -1
    return sequentialSearchRec(alist, item, index + 1)

# Problem 2

def binarySearchRec(alist, item, first=None, last=None):
    # Default parameters
    if first == None or last == None:
        (first, last) = (first or 0, last or len(alist) - 1)

    if first > last:
        return False # OR return -1
    midpoint = (first + last) // 2
    if alist[midpoint] == item:
        return True  # OR return midpoint

    if item < alist[midpoint]:
        (first, last) = (first, midpoint - 1)
    else:
        (first, last) = (midpoint + 1, last)
    return binarySearchRec(alist, item, first, last)
