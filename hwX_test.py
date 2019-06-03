#!/usr/bin/python3
# Homework 5 Unit Tests

import unittest
import random
import functools


def isIncreasing(iter):
    for i in range(len(iter)-1):
        if iter[i] > iter[i+1]:
            return False
    return True
def isDecreasing(iter):
    for i in range(len(iter)-1):
        if iter[i] < iter[i+1]:
            return False
    return True

def misplacedItems(items):
    for i in range(len(items)-1):
        first = items[i]
        second = items[i+1]
        if first[1] > second[1]:
            return first,second
        if first[1] == second[1]:
            if first[0] > second[0]:
                return first,second
    return None


def rightPadName(name, length, char=" "):
    nameStr = name[0] + " " + name[1]
    return rightPad(nameStr, length, char)

def rightPad(string, length, char=" "):
    return string + (char * (length - len(string)))

def column_print(original, sorted, expected, label):
    columnWidth = 16

    print("%s        %s        %s" % (rightPad("Sorted List:", columnWidth), rightPad(label+":", columnWidth), rightPad("Expected Order:", columnWidth)))
    for o_item, s_item, e_item in zip(original, sorted, expected):
        print("    %s        %s        %s" % (rightPadName(o_item, columnWidth), rightPadName(s_item, columnWidth), rightPadName(e_item, columnWidth)))


sorted_students = [ ("Jane","Liu"), ("Ruining","Liu"), ("Ryan","Liu"), ("Yuxin","Liu"), ("Ziwei","Liu"),
                    ("Caitlyn","Nguyen"), ("Mangiu","Nguyen"), ("Martin","Nguyen"), ("Matthew","Nguyen"), ("Weishen","Nguyen"),
                    ("Anthony","Yang"), ("Duc","Yang"), ("Kevin","Yang"), ("Tony","Yang"), ("Trisha","Yang")]

students = [('Yuxin', 'Liu'), ('Anthony', 'Yang'), ('Ryan', 'Liu'), ('Kevin', 'Yang'), ('Matthew', 'Nguyen'), ('Weishen', 'Nguyen'), ('Tony', 'Yang'), ('Duc', 'Yang'), ('Martin', 'Nguyen'), ('Mangiu', 'Nguyen'), ('Jane', 'Liu'), ('Caitlyn', 'Nguyen'), ('Ziwei', 'Liu'), ('Trisha', 'Yang'), ('Ruining', 'Liu')]



class TestProblem1(unittest.TestCase):

    def test_API(self):
        '''P1: Sanity Test: Is mergesort callable?'''
        from hwX import mergesort
        mergesort([(1,1),(2,2),(3,3)])

    def test_sortNames(self):
        '''P1: Sorting a list of names'''
        from hwX import mergesort

        items = sorted(students) # This will sort all students by first name
        items = mergesort(items) # Hopefully, this stably sorts by last name

        print("\nSorted with Merge Sort")
        column_print(sorted(students), items, sorted_students, "After Merge Sort")

        #self.assertEqual(items, sorted_students, "Students should be sorted by last name, not by first name.")
        # Keep the output terse
        stableOrder = items == sorted_students
        self.assertTrue(stableOrder, 'Students should be sorted by last name; "Sorted" and "Expected" values should match in printout.')

    def test_sortRandomValues(self):
        '''P1: Sorting a list of random values'''
        from hwX import mergesort

        items = [(random.randint(0,15), random.randint(0,15)) for i in range(256)]
        items.sort() # Default sort is by first index.
        items = mergesort(items) # Sort by second index

        if isIncreasing(items):
            raise unittest.SkipTest("Not attempted yet")

        self.assertIsNone(misplacedItems(items), "These items were not properly sorted; the first should not preceed the second when properly sorted.")


class TestProblem2(unittest.TestCase):

    def test_API(self):
        '''P2: Sanity Test: Is selectionSort callable?'''
        from hwX import selectionSort
        selectionSort([(1,1),(2,2),(3,3)])

    def test_sortNames(self):
        '''P2: Sorting a list of names'''
        from hwX import selectionSort

        items = sorted(students) # This will sort all students by first name
        selectionSort(items) # This sorts by last name, but might shuffle first names!

        print("\nSorted with Selection Sort")
        column_print(sorted(students), items, sorted_students, "After Sel. Sort")
        print("Selection Sort is not stable, so it will not match the 'Expected Output' column.")

        second_values = [item[1] for item in items]
        self.assertTrue(isIncreasing(second_values), "The last names need to be sorted, regardless of whether or not the sort is stable.")
        # Keep the output terse
        stableOrder = items == sorted_students
        self.assertFalse(stableOrder, 'selectionSort is unstable, so students sorted by last name will lose the first-name ordering; "Sorted" and "Expected" values should not match in printout.')

    def test_sortRandomValues(self):
        '''P2: Sorting a list of random values'''
        from hwX import selectionSort

        items = [(random.randint(0,15), random.randint(0,15)) for i in range(256)]
        items.sort() # Default sort is by first index.
        selectionSort(items) # Sort by second index

        if isIncreasing(items):
            raise unittest.SkipTest("Not attempted yet")

        second_values = [item[1] for item in items]
        self.assertTrue(isIncreasing(second_values), "The second items need to be sorted, regardless of whether or not the sort is stable.")
        self.assertIsNotNone(misplacedItems(items), "SelectionSort (as discussed in class) is not stable; the ordering of first items will not be preserved")


class TestProblem3(unittest.TestCase):

    def test_API(self):
        '''P3: Sanity Test: Are the answers defined and do they have the correct length?'''
        from hwX import problem3_part1
        from hwX import problem3_part2
        from hwX import problem3_part3

        if len(problem3_part1) == 0:
            raise unittest.SkipTest("Not attempted yet")
        self.assertEqual(len(problem3_part1), 10, "The heap for problem 3 part 1 has 10 items in it. So should the list representation.")
        for item in problem3_part1:
            self.assertIsInstance(item, int, "All items in solutions to problems 3 and 4 must be integers")

        if len(problem3_part2) == 0:
            raise unittest.SkipTest("Not attempted yet")
        self.assertEqual(len(problem3_part2), 11, "The heap for problem 3 part 2 has 11 items in it (10 items, then one was added). So should the list representation.")
        for item in problem3_part2:
            self.assertIsInstance(item, int, "All items in solutions to problems 3 and 4 must be integers")

        if len(problem3_part3) == 0:
            raise unittest.SkipTest("Not attempted yet")
        self.assertEqual(len(problem3_part3), 9, "The heap for problem 3 part 3 has 9 items in it (10 items, then one was removed). So should the list representation.")
        for item in problem3_part3:
            self.assertIsInstance(item, int, "All items in solutions to problems 3 and 4 must be integers")

class TestProblem4(unittest.TestCase):

    def test_API(self):
        '''P4: Sanity Test: Are the values defined and do they have the correct length?'''
        from hwX import problem4_inorder_traversal
        from hwX import problem4_preorder_traversal
        from hwX import problem4_postorder_traversal
        from hwX import problem4_levelorder_traversal

        if len(problem4_inorder_traversal) == 0:
            raise unittest.SkipTest("Not attempted yet")
        self.assertEqual(len(problem4_inorder_traversal), 15, "The tree has 15 elements; any traversal will be the same length.")
        for item in problem4_inorder_traversal:
            self.assertIsInstance(item, int, "All items in solutions to problems 3 and 4 must be integers")

        if len(problem4_preorder_traversal) == 0:
            raise unittest.SkipTest("Not attempted yet")
        self.assertEqual(len(problem4_preorder_traversal), 15, "The tree has 15 elements; any traversal will be the same length.")
        for item in problem4_preorder_traversal:
            self.assertIsInstance(item, int, "All items in solutions to problems 3 and 4 must be integers")

        if len(problem4_postorder_traversal) == 0:
            raise unittest.SkipTest("Not attempted yet")
        self.assertEqual(len(problem4_postorder_traversal), 15, "The tree has 15 elements; any traversal will be the same length.")
        for item in problem4_postorder_traversal:
            self.assertIsInstance(item, int, "All items in solutions to problems 3 and 4 must be integers")

        if len(problem4_levelorder_traversal) == 0:
            raise unittest.SkipTest("Not attempted yet")
        self.assertEqual(len(problem4_levelorder_traversal), 15, "The tree has 15 elements; any traversal will be the same length.")
        for item in problem4_levelorder_traversal:
            self.assertIsInstance(item, int, "All items in solutions to problems 3 and 4 must be integers")


if __name__ == "__main__":
    try:
        unittest.main(exit=False, verbosity=2)
    except:
        import traceback
        traceback.print_exc()

    input("Press ENTER to dismiss...")
