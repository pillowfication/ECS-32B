#!/usr/bin/python3
# Homework 6 Unit Tests

import unittest
import re
import sys


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

class OutputThief:
    ''' Replace sys.stdout with self, stealing any output to print statements.
            Only active inside of a with block '''
    def __init__(self):
        self.writes = []

    # Replace sys.stdout with self; put it back when we exit
    def __enter__(self):
        self.old_output = sys.stdout
        sys.stdout = self
        return self
    def __exit__(self, type, value, traceback):
        sys.stdout = self.old_output

    # Any writes that would have been made are instead saved internally
    def write(self, message):
        self.writes.append(message)

    # If any other methods (flush, etc) get called, ignore 'em
    def __getattr__(self, attrib):
        pass

    # Return all of the write operations, concatenated, as a single string
    def getOutput(self):
        return "".join(self.writes)

def symbolsInOrder(symbols, string):
    '''Helper function to determine whether or not the given symbols appear in the target string,
            potentially separated by whitespace.'''
    regex = "\\s*".join(map(re.escape, symbols))
    return re.search(regex, string) is not None


class TestProblem1(unittest.TestCase):

    def test_API(self):
        '''P1: Sanity Test: Is expTree defined?'''
        from hw6 import expTree

        if expTree is None:
            raise unittest.SkipTest("Not attempted yet")

    def test_items(self):
        '''P1: Are all of the values and operations in the resulting expression?'''
        from hw6 import expTree

        if expTree is None:
            raise unittest.SkipTest("Not attempted yet")

        expr = str(expTree)

        self.assertIn("+", expr, "+ is missing from the resulting expression")
        self.assertIn("/", expr, "/ is missing from the resulting expression")
        self.assertIn("*", expr, "* is missing from the resulting expression")
        self.assertIn("-", expr, "- is missing from the resulting expression")

        self.assertIn("1", expr, "1 is missing from the resulting expression")
        self.assertIn("2", expr, "2 is missing from the resulting expression")
        self.assertIn("3", expr, "3 is missing from the resulting expression")
        self.assertIn("5", expr, "5 is missing from the resulting expression")

    def test_expression(self):
        '''P1: Is the resulting expression correct (ignoring parentheses)?'''
        from hw6 import expTree

        if expTree is None:
            raise unittest.SkipTest("Not attempted yet")

        expr = str(expTree)
        expr = removeWhitespace(expr)
        expr = expr.replace("(", "").replace(")", "") # remove parens
        self.assertTrue(symbolsInOrder("3+1/2*5-2", expr), "Expression is incorrect. The printexp() can assist in ensuring you have built the correct expression tree.")

class TestProblem2(unittest.TestCase):

    def test_API(self):
        '''P2: Sanity Test: Are preorder, inorder, and postorder callable?'''
        from hw6 import ExpTree
        from hw6 import preorder, inorder, postorder

        try:
            preorder(ExpTree("0"))
            inorder(ExpTree("0"))
            postorder(ExpTree("0"))
        except NotImplementedError:
            raise unittest.SkipTest("Not attempted yet")

    def test_problemOnePre(self):
        '''P2: Does preorder() work on the result of problem 1?'''
        from hw6 import expTree
        from hw6 import preorder

        if expTree is None:
            raise unittest.SkipTest("Problem 1 not attempted yet")

        with OutputThief() as thief:
            preorder(expTree)
        self.assertTrue(symbolsInOrder("*+3/12-52", thief.getOutput()), "Pre-order traversal of Problem 1 expression tree is incorrect")

    def test_problemOneIn(self):
        '''P2: Does inorder() work on the result of problem 1?'''
        from hw6 import expTree
        from hw6 import inorder

        if expTree is None:
            raise unittest.SkipTest("Problem 1 not attempted yet")

        with OutputThief() as thief:
            inorder(expTree)
        self.assertTrue(symbolsInOrder("3+1/2*5-2", thief.getOutput()), "In-order traversal of Problem 1 expression tree is incorrect")

    def test_problemOnePost(self):
        '''P2: Does inorder() work on the result of problem 1?'''
        from hw6 import expTree
        from hw6 import postorder

        if expTree is None:
            raise unittest.SkipTest("Problem 1 not attempted yet")

        with OutputThief() as thief:
            postorder(expTree)
        self.assertTrue(symbolsInOrder("312/+52-*", thief.getOutput()), "Post-order traversal of Problem 1 expression tree is incorrect")

    @skip_when_not_implemented
    def test_hardProblem(self):
        '''P2: Do preorder(), inorder(), and postorder() work for a harder expression tree?'''
        from hw6 import ExpTree
        from hw6 import preorder, inorder, postorder

        expTree = ExpTree("-")

        expTree.setLeftChild( ExpTree("+") )
        expTree.getLeftChild().setLeftChild( ExpTree("+") )
        expTree.getLeftChild().setRightChild( ExpTree(1000) )
        expTree.getLeftChild().getLeftChild().setLeftChild( ExpTree("+") )
        expTree.getLeftChild().getLeftChild().setRightChild( ExpTree(100) )
        expTree.getLeftChild().getLeftChild().getLeftChild().setLeftChild( ExpTree(1) )
        expTree.getLeftChild().getLeftChild().getLeftChild().setRightChild( ExpTree(10) )

        expTree.setRightChild( ExpTree("*") )
        expTree.getRightChild().setLeftChild( ExpTree(22) )
        expTree.getRightChild().setRightChild( ExpTree("/") )
        expTree.getRightChild().getRightChild().setLeftChild( ExpTree(88) )
        expTree.getRightChild().getRightChild().setRightChild( ExpTree(16) )

        with OutputThief() as thief:
            preorder(expTree)
        output = thief.getOutput()
        self.assertTrue(symbolsInOrder("-+++1101001000*22/8816", output), "Pre-order traversal of expression tree is incorrect")
        for value in [1,10,100,1000,22,88,16]:
            self.assertIn(str(value), output, "All terms from the expression tree should be in the output traversal")
        for digits in ["11", "01", "28", "81"]:
            self.assertNotIn(digits, output, "Numerical values must be separated by spaces!")

        with OutputThief() as thief:
            inorder(expTree)
        output = thief.getOutput()
        self.assertTrue(symbolsInOrder("1+10+100+1000-22*88/16", output), "In-order traversal of expression tree is incorrect")
        for value in [1,10,100,1000,22,88,16]:
            self.assertIn(str(value), output, "All terms from the expression tree should be in the output traversal")
        for digits in ["11", "01", "28", "81"]:
            self.assertNotIn(digits, output, "Numerical values must be separated by spaces!")

        with OutputThief() as thief:
            postorder(expTree)
        output = thief.getOutput()
        self.assertTrue(symbolsInOrder("110+100+1000+228816/*-", output), "Post-order traversal of expression tree is incorrect")
        for value in [1,10,100,1000,22,88,16]:
            self.assertIn(str(value), output, "All terms from the expression tree should be in the output traversal")
        for digits in ["11", "01", "28", "81"]:
            self.assertNotIn(digits, output, "Numerical values must be separated by spaces!")


def removeWhitespace(string):
    for char in [" ", "\t", "\r", "\n"]:
        string = string.replace(char, "")
    return string

class TestProblem3(unittest.TestCase):

    def test_API(self):
        '''P3: Sanity Test: Is printexp still callable?'''
        from hw6 import ExpTree
        from hw6 import printexp

        printexp(ExpTree("0"))

    def test_problemOneInput(self):
        '''P3: Ensure proper round-trip from expression given in problem 1'''
        from hw6 import printexp
        from hw6 import expTree

        if expTree is None:
            raise unittest.SkipTest("Problem 1 not attempted yet")

        result = printexp(expTree)
        result = removeWhitespace(result)
        self.assertEqual(result, "((3+(1/2))*(5-2))", "printexp() should give the original expression from problem 1 when run on expTree")


class TestProblem4(unittest.TestCase):

    def test_API(self):
        '''P4: Sanity Test: Are the answers defined and do they have the correct length?'''
        from hw6 import problem4_breadth_first_traversal
        from hw6 import problem4_depth_first_traversal

        if len(problem4_breadth_first_traversal) <= 1:
            raise unittest.SkipTest("Not attempted yet")
        self.assertEqual(len(problem4_breadth_first_traversal), 9, "The graph has 9 nodes; the traversal should also have 9 items")
        for item in problem4_breadth_first_traversal:
            self.assertIsInstance(item, int, "All items in solutions to problem 4 must be integers")
        self.assertEqual(problem4_breadth_first_traversal[0], 0, "The first item in the traversal should be the starting node: 0")

        if len(problem4_depth_first_traversal) <= 1:
            raise unittest.SkipTest("Not attempted yet")
        self.assertEqual(len(problem4_depth_first_traversal), 9, "The graph has 9 nodes; the traversal should also have 9 items")
        for item in problem4_depth_first_traversal:
            self.assertIsInstance(item, int, "All items in solutions to problem 4 must be integers")
        self.assertEqual(problem4_depth_first_traversal[0], 0, "The first item in the traversal should be the starting node: 0")


class TestProblem5(unittest.TestCase):

    def test_API(self):
        '''P5: Sanity Test: Has flights graph been defined?'''
        from hw6 import flights

        if flights.numVertices == 0:
            raise unittest.SkipTest("Not attempted yet")

    def test_flightToSFO(self):
        '''P5: Is the flight to San Francisco calculated correctly?'''
        from hw6 import flights

        if flights.numVertices == 0:
            raise unittest.SkipTest("Not attempted yet")

        self.assertEqual(47, flights.getVertex('SFO').getDistance())

    def test_flightToLAX(self):
        '''P5: Is the flight to Los Angeles calculated correctly?'''
        from hw6 import flights

        if flights.numVertices == 0:
            raise unittest.SkipTest("Not attempted yet")

        self.assertEqual(96, flights.getVertex('LAX').getDistance())

    def test_flightToLAS(self):
        '''P5: Is the flight to Las Vegas calculated correctly?'''
        from hw6 import flights

        if flights.numVertices == 0:
            raise unittest.SkipTest("Not attempted yet")

        self.assertEqual(145, flights.getVertex('LAS').getDistance())

    def test_flightToPHX(self):
        '''P5: Is the flight to Phoenix calculated correctly?'''
        from hw6 import flights

        if flights.numVertices == 0:
            raise unittest.SkipTest("Not attempted yet")

        self.assertEqual(194, flights.getVertex('PHX').getDistance())

if __name__ == "__main__":
    try:
        unittest.main(exit=False, verbosity=2)
    except:
        import traceback
        traceback.print_exc()

    input("Press ENTER to dismiss...")
