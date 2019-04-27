#!/usr/bin/python3
# Homework 3 Unit Tests

import unittest
import random

from Node import Node

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


class TestProblem1(unittest.TestCase):

    def test_API(self):
        '''P1: Sanity Test: Is findSmallest callable?'''
        try:
            findSmallest([1,2,3])
        except NotImplementedError:
            raise unittest.SkipTest("findSmallest has not been implemented yet")
        except:
            self.fail("Error while calling findSmallest")

    @skip_when_not_implemented
    def test_oneArg(self):
        '''P1: Single-value test'''
        self.assertEqual(5, findSmallest([5]), "Incorrect minimum of single-item list")

    @skip_when_not_implemented
    def test_twoArgs(self):
        '''P1: Two-value test'''
        self.assertEqual(5, findSmallest([10,5]), "Incorrect minimum of two-item list")
        self.assertEqual(5, findSmallest([5,10]), "Incorrect minimum of two-item list")

    @skip_when_not_implemented
    def test_tenArgs(self):
        '''P1: Ten-value test'''
        self.assertEqual(0, findSmallest(list(range(10))), "Incorrect minimum of increasing list")
        self.assertEqual(0, findSmallest(list(range(10))[::-1]), "Incorrect minimum of decreasing list")
        values = list(range(10))
        random.shuffle(values)
        self.assertEqual(0, findSmallest(values), "Incorrect minimum of randomized list")


def makeLinkedList(items):
    if len(items) == 0:
        return None

    node = Node(items[0])
    node.setNext(makeLinkedList(items[1:]))

    return node

class TestProblem2(unittest.TestCase):

    def test_API(self):
        '''P2: Sanity Test: Is findValue callable?'''
        try:
            findValue(2, makeLinkedList([1,2,3]))
        except NotImplementedError:
            raise unittest.SkipTest("findValue has not been implemented yet")
        except:
            self.fail("Error while calling findValue")

    @skip_when_not_implemented
    def test_findHead(self):
        '''P2: Find head of linked list'''
        items = makeLinkedList([1,2,3])
        self.assertTrue(findValue(1, items), "Failed to find head of linked list")

    @skip_when_not_implemented
    def test_findMid(self):
        '''P2: Find middle of linked list'''
        items = makeLinkedList([2,1,3])
        self.assertTrue(findValue(1, items), "Failed to find middle of linked list")

    @skip_when_not_implemented
    def test_findTail(self):
        '''P2: Find end of linked list'''
        items = makeLinkedList([3,2,1])
        self.assertTrue(findValue(1, items), "Failed to find tail of linked list")

    @skip_when_not_implemented
    def test_cantFindSingle(self):
        '''P2: Failed search in a single-item list'''
        items = makeLinkedList([2])
        self.assertFalse(findValue(1, items), "Found a value that isn't in the list")

    @skip_when_not_implemented
    def test_cantFindMultiple(self):
        '''P2: Failed search in a single-item list'''
        items = makeLinkedList([5,6,7])
        self.assertFalse(findValue(1, items), "Found a value that isn't in the list")


class TestProblem3(unittest.TestCase):

    def test_API(self):
        '''P3: Sanity Test: Is ladder callable?'''
        try:
            ladder(3)
        except NotImplementedError:
            raise unittest.SkipTest("ladder has not been implemented yet")
        except:
            self.fail("Error while calling ladder")

    @skip_when_not_implemented
    def test_baseCases(self):
        '''P3: Ladder base cases'''
        self.assertEqual(1, ladder(1), "There is only one way to climb a 1-rung ladder")
        self.assertEqual(2, ladder(2), "There are two ways to climb a 2-rung ladder")

    @skip_when_not_implemented
    def test_examples(self):
        '''P3: Ladder example cases'''
        self.assertEqual(3, ladder(3), "There are 3 ways to climb a 3-rung ladder")
        self.assertEqual(8, ladder(5), "There are 8 ways to climb a 5-rung ladder")
        self.assertEqual(89, ladder(10), "There are 89 ways to climb a 10-rung ladder")

    @skip_when_not_implemented
    def test_large(self):
        '''P3: Long ladder test'''
        self.assertEqual(1346269, ladder(30), "There are 1,346,269 ways to climb a 30-rung ladder")


class TestProblem4(unittest.TestCase):

    def test_API(self):
        '''P4: Sanity Test: Is recPal callable?'''
        try:
            recPal("x")
        except NotImplementedError:
            raise unittest.SkipTest("recPal has not been implemented yet")
        except:
            self.fail("Error while calling recPal")

    @skip_when_not_implemented
    def test_singlePass(self):
        '''P4: Single-letter test'''
        self.assertTrue(recPal("x"), "A single-letter string is always a palindrome")

    @skip_when_not_implemented
    def test_doublePass(self):
        '''P4: Double-letter passing test'''
        self.assertTrue(recPal("xx"), "A pair of the same letter is a palindrome")

    @skip_when_not_implemented
    def test_doubleFail(self):
        '''P4: Double-letter failing test'''
        self.assertFalse(recPal("AB"), "Two different letters do not form a valid palindrome")

    @skip_when_not_implemented
    def test_longPass(self):
        '''P4: Long palindrome'''
        length = 128

        # random capital letters, not including the letter Z
        longstr = "".join( chr(random.randint(ord("A"), ord("Y"))) for i in range(length))
        # Add the string to itself, reversed
        longstr += longstr[::-1]

        self.assertTrue(recPal(longstr), "A very long string appended to it's own reverse is a palindrome")

    @skip_when_not_implemented
    def test_longFail(self):
        '''P4: Long palindrome with a single-character error'''
        length = 128

        # random capital letters, not including the letter Z
        longstr = "".join( chr(random.randint(ord("A"), ord("Y"))) for i in range(length))
        # Add the string to itself, reversed
        longstr += longstr[::-1]

        # Break the palindrome!
        random_index = random.randint(length//2, length + length//2)
        # Strings don't support assignment, so this won't work:
        #   longstr[ random_index ] = "Z"
        # Instead, build a new string from the pieces of the old one:
        longstr = longstr[:random_index] + "Z" + longstr[random_index+1:]

        # If the palindrome was odd-length, there is a position where
        #   a single-character error could still be a palindrome....
        self.assertFalse(recPal(longstr), "An even-length palindrome with any single-character error is no longer a palindrome")



if __name__ == "__main__":
    try:
        from hw3 import findSmallest
        from hw3 import findValue
        from hw3 import ladder
        from hw3 import recPal

        unittest.main(exit=False, verbosity=2)
    except ModuleNotFoundError:
        print("Unable to import functions or classes from hw3.py. Please ensure that hw3.py and Node.py are located in the same directory as this test file, and that all classes and functions are named correctly.")
    except:
        import traceback
        traceback.print_exc()
    input("Press ENTER to dismiss...")
