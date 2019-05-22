#!/usr/bin/python3
# Homework 5 Unit Tests

import unittest
import random

from hw5 import insertionSort
from hw5 import bubbleSort
from hw5 import selectionSortK
from hw5 import mergeSort
from BinarySearchTree import BinarySearchTree



class NotAllowed(Exception):
    pass

class StrictList:
    def __init__(self, iter=None):
        self.list = []
        if iter is not None:
            self.list.extend(iter)
        self.reads = 0
        self.writes = 0
        self.updates = 0

    def __getitem__(self, index):
        if isinstance(index, slice):
            raise NotAllowed("You should not be using slicing for this assignment!")
        else:
            self.reads += 1
            return self.list[index]

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            raise NotAllowed("You should not be using slicing for this assignment!")
        else:
            self.writes += 1
            if self.list[index] != value:
                self.list[index] = value
                self.updates += 1

    def __contains__(self, item):
        raise NotAllowed("No credit for built-in search")

    def __len__(self):
        return len(self.list)

class SwapList(StrictList):
    def __init__(self, iter=None, adj=False):
        super().__init__(iter)
        self.prev_accesses = []
        self.adj = adj

    def __getitem__(self, index):
        if isinstance(index, slice):
            raise NotAllowed("You should not be using slicing for this assignment!")
        else:
            self.reads += 1
            self.prev_accesses.insert(0, index)
            if len(self.prev_accesses) > 2:
                self.prev_accesses.pop(2)

            return self.list[index]

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            raise NotAllowed("You should not be using slicing for this assignment!")
        else:
            if index not in self.prev_accesses:
                raise NotAllowed("This list must be sorted using only swap operations.")
            if self.adj:
                if abs(self.prev_accesses[0]-self.prev_accesses[1]) != 1:
                    raise NotAllowed("Swap operations must only be performed on adjacent items.")

            self.writes += 1
            if self.list[index] != value:
                self.list[index] = value
                self.updates += 1


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


class TestProblem1(unittest.TestCase):

    def test_API(self):
        '''P1: Sanity Test: Is insertionSort callable?'''
        try:
            insertionSort([1,2,3])
        except:
            self.fail("Error while calling insertionSort")

    def test_sortRandomValues(self):
        '''P1: Sorting a list of random values'''
        items = StrictList([random.randint(0,2**30) for i in range(1024)])
        insertionSort(items)

        if isIncreasing(items):
            raise unittest.SkipTest("Not implemented yet")

        self.assertTrue(isDecreasing(items), "Items need to be sorted in decreasing order")

    def test_sortDecreasingValues(self):
        '''P1: Sorting a list that is already sorted'''
        items = StrictList(range(1023,-1,-1))
        insertionSort(items)

        if isIncreasing(items):
            raise unittest.SkipTest("Not implemented yet")

        self.assertTrue(isDecreasing(items), "Items need to be sorted in decreasing order")
        self.assertEqual(0, items.updates, "No modifications should be made to a list that is already sorted")

class TestProblem2(unittest.TestCase):

    def test_API(self):
        '''P2: Sanity Test: Is bubbleSort callable?'''
        try:
            bubbleSort([1,2,3])
        except:
            self.fail("Error while calling bubbleSort")

    def test_sortRandomValues(self):
        '''P2: Sorting a list of random values'''
        items = SwapList([random.randint(0,2**30) for i in range(1024)], adj=True)
        bubbleSort(items)

        if isIncreasing(items):
            raise unittest.SkipTest("Not implemented yet")

        self.assertTrue(isDecreasing(items), "Items need to be sorted in decreasing order")

    def test_sortDecreasingValues(self):
        '''P2: Sorting a list that is already sorted'''
        items = SwapList(range(1023,-1,-1), adj=True)
        bubbleSort(items)

        if isIncreasing(items):
            raise unittest.SkipTest("Not implemented yet")

        self.assertTrue(isDecreasing(items), "Items need to be sorted in decreasing order")
        self.assertEqual(0, items.writes, "No swaps should be performed for a list that is already sorted")

class TestProblem3(unittest.TestCase):

    def test_API(self):
        '''P3: Sanity Test: Is selectionSortK callable?'''
        try:
            selectionSortK([1,2,3], 2)
        except:
            self.fail("Error while calling selectionSortK")

    def test_doNothing(self):
        '''P3: Does sorting the first k elements with k=0 do nothing?'''
        items = [3,2,4,1,5]
        selectionSortK(items, 0)

        self.assertEqual(items, [3,2,4,1,5], "Calling selectionSortK with K=0 should do nothing!")

    def test_severalPasses(self):
        '''P3: Sorting a decreasing list in several stages'''

        # If do-nothing fails, skip this test...
        items = [3,2,4,1,5]
        selectionSortK(items, 0)
        if items != [3,2,4,1,5]:
            raise unittest.SkipTest("Not implemented yet")


        stage_items = 256
        stage_count = 4

        items = SwapList([random.randint(0,2**30) for i in range(stage_items * stage_count)])
        sorted_items = []

        for stage in range(stage_count):
            selectionSortK(items, stage_items)

            remaining_items = []
            for i in range(stage_items):
                sorted_items.append(items[i])
            for i in range(stage_items, len(items)):
                remaining_items.append(items[i])
            if remaining_items:
                items = SwapList(remaining_items)

        self.assertTrue(isIncreasing(sorted_items))

    def test_onePass(self):
        '''P3: Sorting a portion of a decreasing list'''

        # If do-nothing fails, skip this test...
        items = [3,2,4,1,5]
        selectionSortK(items, 0)
        if items != [3,2,4,1,5]:
            raise unittest.SkipTest("Not implemented yet")


        count = 256
        items = SwapList(range(count,-1,-1))

        chunk = count//3

        selectionSortK(items, chunk)

        for i in range(chunk-1):
            self.assertLess(items[i], items[i+1], "The first K items should be sorted")
        for i in range(chunk, count):
            self.assertLess(items[chunk-1], items[i], "All values in the unsorted portion of the list should be larger than the sorted items")

        remaining_items = []
        for i in range(chunk, count):
            remaining_items.append(items[i])
        self.assertTrue(not isIncreasing(remaining_items), "Items after the first K should not have been sorted!")

class TestProblem4(unittest.TestCase):

    def test_API(self):
        '''P4: Sanity Test: Is mergeSort callable?'''
        try:
            mergeSort([1,2,3])
        except:
            self.fail("Error while calling mergeSort")

    def test_sortRandomValues(self):
        '''P4: Sorting a list of random values'''
        original_items = [random.randint(0,2**30) for i in range(1024)]
        items = StrictList(original_items)
        mergeSort(items)

        if items.reads == 0:
            raise unittest.SkipTest("Not implemented yet")

        self.assertTrue(isIncreasing(items), "Items need to be sorted in increasing order")

    def test_sortIncreasingValues(self):
        '''P4: Sorting a list that is already sorted'''
        items = StrictList(range(1024))
        mergeSort(items)

        if items.reads == 0:
            raise unittest.SkipTest("Not implemented yet")

        self.assertTrue(isIncreasing(items), "Items need to be sorted in increasing order")
        self.assertNotEqual(0, items.writes, "MergeSort performs the same operations regardless of input order")

class TestProblem5(unittest.TestCase):

    def test_API(self):
        '''P5: Sanity Test: Is BinarySearchTree constructable?'''
        try:
            BinarySearchTree()
        except:
            self.fail("Error while constructing a BinarySearchTree")

    def test_storeAndLoad(self):
        '''P5: Can items be stored and retrieved from the BinarySearchTree?'''
        itemcount = 26
        items = []
        for i in range(itemcount):
            items.append( (i,chr(ord("a")+i)) )

        random.shuffle(items) # Insert in a random order
        bintree = BinarySearchTree()
        for key,value in items:
            bintree[key] = value

        self.assertEqual(itemcount, len(bintree), "After inserting %d items, the tree size should be %d, not %d" % (itemcount, itemcount, len(bintree)))

        random.shuffle(items) # Retrieve in a random order
        for key,value in items:
            retrievedVal = bintree[key]
            self.assertEqual(value, retrievedVal, "Item inserted as key,value = (%r,%r) retrieved as (%r,%r)" % (key,value,key,retrievedVal))

        self.assertEqual(itemcount, len(bintree), "After accessing items, the tree size should not change.")

    def test_updates(self):
        '''P5: Can items be updated in the BinarySearchTree?'''
        itemcount = 64
        items = []
        for i in range(1,itemcount+1):
            items.append( (i,i**2) )

        random.shuffle(items) # Insert in a random order
        bintree = BinarySearchTree()
        for key,value in items:
            bintree[key] = value

        self.assertEqual(itemcount, len(bintree), "After inserting %d items, the tree size should be %d, not %d" % (itemcount, itemcount, len(bintree)))

        random.shuffle(items) # Retrieve in a random order
        for key,value in items:
            retrievedVal = bintree[key]
            self.assertEqual(value, retrievedVal, "Item inserted as key,value = (%r,%r) retrieved as (%r,%r)" % (key,value,key,retrievedVal))

        self.assertEqual(itemcount, len(bintree), "After accessing items, the tree size should not change.")

        items = []
        for i in range(1,itemcount+1):
            items.append( (i,-i**2) )

        random.shuffle(items)
        for key,value in items:
            bintree[key] = value

        self.assertEqual(itemcount, len(bintree), "After updating items, the tree size should not change.")

        random.shuffle(items) # Retrieve in a random order
        for key,value in items:
            retrievedVal = bintree[key]
            self.assertEqual(value, retrievedVal, "After update, item updated to key,value = (%r,%r) retrieved as (%r,%r)" % (key,value,key,retrievedVal))



if __name__ == "__main__":
    try:
        unittest.main(exit=False, verbosity=2)
    except:
        import traceback
        traceback.print_exc()

    input("Press ENTER to dismiss...")
