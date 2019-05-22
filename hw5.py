# Your name and email here
# Markus Tran
# mkhtran@ucdavis.edu

# Problem 1
#   http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html

def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] < currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue

# Problem 2
#   http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBubbleSort.html

def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] < alist[i + 1]:
                (alist[i], alist[i + 1]) = (alist[i + 1], alist[i])

# Problem 3
#   Selection Sort as shown in class: Lecture 19, Slide 45

def selectionSortK(alist, k):
    for i in range(0, k):
        min = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min]:
                min = j
        (alist[i], alist[min]) = (alist[min], alist[i])

# Problem 4
#   http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html

def mergeSort(alist, workspace=None, start=None, end=None):
    if workspace is None:
        start = 0
        end = len(alist)
        workspace = [None] * end

    if end - start <= 1:
        return

    midpoint = (start + end) // 2

    mergeSort(alist, workspace, start, midpoint)
    mergeSort(alist, workspace, midpoint, end)

    # Merge into the workspace
    pointer1 = start
    pointer2 = midpoint

    for i in range(start, end):
        if pointer1 != midpoint and (pointer2 == end or alist[pointer1] <= alist[pointer2]):
            workspace[i] = alist[pointer1]
            pointer1 += 1
        else:
            workspace[i] = alist[pointer2]
            pointer2 += 1

    # Copy workspace into array
    for i in range(start, end):
        alist[i] = workspace[i]
