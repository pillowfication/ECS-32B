
# Problem 1
#   http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html

def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

# Problem 2
#   http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBubbleSort.html

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# Problem 3
#   Selection Sort as shown in class: Lecture 19, Slide 45

def selectionSortK(alist, k):
    for i in range(0,len(alist) - 1):
        min = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min]:
                min = j
        temp = alist[i]
        alist[i] = alist[min]
        alist[min] = temp

# Problem 4
#   http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html

def mergeSort(alist, workspace=None, start=None, end=None):

    #### You can change this code if you want to, but it sufficient to implement a solution.

    if workspace is None:
        workspace = [None] * len(alist)
        start = 0
        end = len(alist) #### Note that end is not a valid index into the array -- it's one past the last element!

    if end-start <= 1:
        return

    midpoint = (start+end)//2

    mergeSort(alist, workspace, start, midpoint)
    mergeSort(alist, workspace, midpoint, end)

    #### From here on, the code will look very similar to the code from the textbook
    ####    Be sure you understand what the code is doing before you copy it over!
    ####    Remember to copy the data back from the workspace!
