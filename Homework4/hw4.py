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
    raise NotImplementedError
