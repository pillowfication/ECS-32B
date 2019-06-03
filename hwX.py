# ECS32B Spring 2019, Makeup Assignment
# Your Name Here!
# Markus Tran
# mkhtran@ucdavis.edu

# Problem 1
#   Lecture 20 Slides, #40: https://canvas.ucdavis.edu/courses/333631/files?preview=6021636

def mergesort(mlist):
    if len(mlist) < 2:
        return mlist
    else:
        mid = len(mlist) // 2
        return merge(mergesort(mlist[:mid]), mergesort(mlist[mid:]))

# merge two sorted lists
def merge(left, right):
    if left == []:
        return right
    elif right == []:
        return left
    elif left[0][1] <= right[0][1]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])

# Problem 2
#   Lecture 19 Slides, #45: https://canvas.ucdavis.edu/courses/333631/files?preview=6001204

## selection sort not from book - note that we're just calling it selectionSort!
def selectionSort(alist):
    for i in range(0, len(alist) - 1):
        min = i
        for j in range(i + 1, len(alist)):
            if alist[j][1] < alist[min][1]:
                min = j
        temp = alist[i]
        alist[i] = alist[min]
        alist[min] = temp

# Problem 3

# Must be valid Python lists!
# example: problem3_part1 = [1,2,3,4]

problem3_part1 = [ 89, 35, 29, 24, 19, 17, 1, 7, 3, 4 ]
problem3_part2 = [ 89, 63, 29, 24, 35, 17, 1, 7, 3, 4, 19 ]
problem3_part3 = [ 35, 24, 29, 7, 19, 17, 1, 4, 3 ]

# Problem 4

problem4_inorder_traversal = [ 1, 2, 3, 9, 22, 34, 36, 28, 42, 56, 55, 60, 77, 79, 80 ]
problem4_preorder_traversal = [ 22, 9, 2, 1, 3, 42, 28, 36, 34, 60, 55, 56, 79, 77, 80 ]
problem4_postorder_traversal = [ 1, 3, 2, 9, 34, 36, 28, 56, 55, 70, 80, 79, 60, 42, 22 ]
problem4_levelorder_traversal = [ 22, 9, 42, 2, 28, 60, 1, 3, 36, 55, 79, 34, 56, 77, 80 ]
