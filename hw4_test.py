#!/usr/bin/python3
# Homework 4 Unit Tests

import unittest
import random
import multiprocessing
import time
import sys


from hw4 import sequentialSearchRec
from hw4 import binarySearchRec
from HashTable import HashTable





# Make a decorator that skips tests when the required functionality hasn't been implemented yet.
def skip_when_not_implemented(func):
    def test(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotImplementedError:
            raise unittest.SkipTest("Not implemented yet")
    # Copy the docstring, so the unit tests give better descriptions.
    test.__doc__ = func.__doc__
    return test

# Test to see if we're currently running in IDLE, where multiprocessing misbehaves.
# Test based on https://stackoverflow.com/questions/3431498/what-code-can-i-use-to-check-if-python-is-running-in-idle
def running_in_idle():
    try:
        # IDLE replaces sys.stdin with a custom class
        return sys.stdin.__module__.startswith("idle")
    except AttributeError:
        return False

# An unmodified HashTable will get stuck in an infinite loop when too many items have been added
# Make a decorator to test for this case, and skip the related tests
def skip_on_infinite_loop(func):
    def test(*args, **kwargs):

        if running_in_idle():
            try:
                print("IDLE may interfere with the testing for this test. If you have not implemented part 2 of question 3, this test will get stuck in an infinite loop. If it gets stuck, press Ctrl+C to skip the test.")
                return func(*args, **kwargs)
            except KeyboardInterrupt:
                raise unittest.SkipTest("Test skipped by user")

        else:
            background_process = multiprocessing.Process(target=hashTableLoopTest)
            background_process.start()
            background_process.join(timeout=5.0) # Wait up to five seconds for this test to complete...

            time.sleep(0.1)
            if background_process.is_alive():
                background_process.terminate()
                raise unittest.SkipTest("If HashTable cannot grow, this test will get stuck in an infinite loop. It will be skipped until you're done with part 2 of question 3.")

            return func(*args, **kwargs)

    # Copy the docstring, so the unit tests give better descriptions.
    test.__doc__ = func.__doc__
    return test

def hashTableLoopTest():
    ht = HashTable()
    for i in range(50):
        ht[i]=i


class NotAllowed(Exception):
    pass

class StrictList:
    def __init__(self, iter=None, parent=None):
        self.list = []
        if iter is not None:
            self.list.extend(iter)
        self.accesses = 0

    def __getattr__(self, methodName):
        print("Delegating method:", methodName)
        return getattr(self.list, methodName)

    def __getitem__(self, index):
        if isinstance(index, slice):
            raise NotAllowed("You should not be using slicing for this assignment!")
        else:
            self.accesses += 1
            return self.list[index]

    def __len__(self):
        return len(self.list)



class TestProblem1(unittest.TestCase):

    def test_API(self):
        '''P1: Sanity Test: Is sequentialSearchRec callable?'''
        try:
            sequentialSearchRec([1,2,3], 2)
        except NotImplementedError:
            raise unittest.SkipTest("sequentialSearchRec has not been implemented yet")
        except:
            self.fail("Error while calling sequentialSearchRec")

    @skip_when_not_implemented
    def test_findHead(self):
        '''P1: Find first element of list'''
        items = StrictList([1,2,3])
        self.assertTrue(sequentialSearchRec(items, 1), "Failed to find head of list")

    @skip_when_not_implemented
    def test_findMid(self):
        '''P1: Find middle element of list'''
        items = StrictList([2,1,3])
        self.assertTrue(sequentialSearchRec(items, 1), "Failed to find middle of list")

    @skip_when_not_implemented
    def test_findTail(self):
        '''P1: Find last element of list'''
        items = StrictList([3,2,1])
        self.assertTrue(sequentialSearchRec(items, 1), "Failed to find tail of list")

    @skip_when_not_implemented
    def test_cantFindSingle(self):
        '''P1: Failed search in a single-item list'''
        items = StrictList([2])
        self.assertFalse(sequentialSearchRec(items, 1), "Found a value that isn't in the list")

    @skip_when_not_implemented
    def test_cantFindMultiple(self):
        '''P1: Failed search in a multiple-item list'''
        items = StrictList([5,6,7])
        self.assertFalse(sequentialSearchRec(items, 1), "Found a value that isn't in the list")


class TestProblem2(unittest.TestCase):

    def test_API(self):
        '''P2: Sanity Test: Is binarySearchRec callable?'''
        try:
            binarySearchRec([1,2,3], 2)
        except NotImplementedError:
            raise unittest.SkipTest("binarySearchRec has not been implemented yet")
        except:
            self.fail("Error while calling binarySearchRec")

    @skip_when_not_implemented
    def test_findHead(self):
        '''P2: Find first element of list'''
        items = StrictList([232,233,234])
        self.assertTrue(binarySearchRec(items, 232), "Failed to find head of list")

    @skip_when_not_implemented
    def test_findMid(self):
        '''P2: Find middle element of list'''
        items = StrictList([231,232,233])
        self.assertTrue(binarySearchRec(items, 232), "Failed to find middle of list")

    @skip_when_not_implemented
    def test_findTail(self):
        '''P2: Find last element of list'''
        items = StrictList([230,231,232])
        self.assertTrue(binarySearchRec(items, 232), "Failed to find tail of list")

    @skip_when_not_implemented
    def test_cantFindSingle(self):
        '''P2: Failed search in a single-item list'''
        items = StrictList([2])
        self.assertFalse(binarySearchRec(items, 232), "Found a value that isn't in the list")

    @skip_when_not_implemented
    def test_findLong(self):
        '''P2: Find element in a very long list'''
        items = StrictList(range(256))
        self.assertTrue(binarySearchRec(items, 232), "Failed to find an element in the list")

    @skip_when_not_implemented
    def test_cantFindLong(self):
        '''P2: Failed search in a very long list'''
        items = StrictList(range(212))
        self.assertFalse(binarySearchRec(items, 232), "Found a value that isn't in the list")

    @skip_when_not_implemented
    def test_ensureBinarySearch(self):
        '''P2: Is binarySearchRec actually performing a binary search?'''
        items = StrictList(range(512))
        self.assertTrue(binarySearchRec(items, 232), "Failed to find an element in the list")
        self.assertLess(items.accesses, 20, "Binary search should only be testing log_2(N) items in a list with N items")


class TestProblem3(unittest.TestCase):

    def test_API(self):
        '''P3: Sanity Test: Is HashTable constructable?'''
        try:
            HashTable()
        except:
            self.fail("Error while constructing HashTable")

    def utility_save_and_restore(self, count):
        ''' Using chr() and ord() is safe for ASCII values [32,127]. Starting at 'A' (65) to keep it printable '''
        items = [(i, chr(ord('A')+i)) for i in range(count)] # (0,'A'), (1,'B'), (2,'C')...

        ht = HashTable()

        for key,value in items:
            ht[key] = value

        for key,value in items:
            self.assertEqual(value, ht[key], "Item not properly stored in HashTable")

    def utility_save_and_restore_random(self, count):
        ''' Assign each index a random integer, test to make sure it survives rehashes. '''
        items = [(i, random.randint(0,2**30)) for i in range(count)] # (0,'?'), (1,'x'), (2,'8')...

        ht = HashTable()

        for key,value in items:
            ht[key] = value

        for key,value in items:
            self.assertEqual(value, ht[key], "Item not properly stored in HashTable")

    @skip_when_not_implemented
    def test_newItemSizes(self):
        '''P3: Does the value returned by empty_slots() decrease as new items are added?'''
        items = [(i, chr(ord('A')+i)) for i in range(9)] # (0,'A'), (1,'B'), (2,'C')...

        ht = HashTable()
        last_empty = ht.empty_slots()

        for key,value in items:
            ht[key] = value
            empty = ht.empty_slots()
            self.assertEqual(last_empty-1, empty, "Adding a new item to the HashTable should reduce the value returned by empty_slots() by one.")
            last_empty = empty

    @skip_when_not_implemented
    def test_updatedItemSizes(self):
        '''P3: Does the value returned by empty_slots() stay the same when items in the HashTable are updated?'''
        items = [(i, chr(ord('A')+i)) for i in range(9)] # (0,'A'), (1,'B'), (2,'C')...

        ht = HashTable()

        for key,value in items:
            ht[key] = value

        final_emptiness = ht.empty_slots()

        for key,value in items:
            ht[key] = value.lower() # (0,'a'), (1,'b')....
            empty = ht.empty_slots()
            self.assertEqual(final_emptiness, empty, "Updating an elemenet of HashTable should not reduce the value returned by empty_slots()")

    def test_withoutResize(self):
        '''P3: Can 11 elements be stored in and recovered from the HashTable?'''
        self.utility_save_and_restore(11)

    @skip_on_infinite_loop
    def test_oneResize(self):
        '''P3: Do elements persist after forcing the HashTable to rehash?'''
        self.utility_save_and_restore(23)

    @skip_on_infinite_loop
    def test_maxSize(self):
        '''P3: Do elements persist after forcing the HashTable to rehash many times?'''
        self.utility_save_and_restore_random(1009)

    @skip_on_infinite_loop
    def test_sizeProgression(self):
        '''P3: Does the table grow in proper size steps?'''
        expected_sizes = set([11,23,53,97,193,389,769,1543])

        ht = HashTable()

        for i in range(1000):
            ht[i] = i
            self.assertTrue(ht.size in expected_sizes, "Hash table size was not one of the suggested primes.")


if __name__ == "__main__":
    try:
        unittest.main(exit=False, verbosity=2)
    except:
        import traceback
        traceback.print_exc()

    if not running_in_idle():
        input("Press ENTER to dismiss...")
