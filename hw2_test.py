#!/usr/bin/python3
# Homework 2 Unit Tests

import unittest
import timeit
import random

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
        '''P1: Sanity Test: Testing the presense of all methods in the Queue Abstract Data Type'''
        try:
            q = QueueFE()
            q.enqueue(1)
            q.dequeue()
            q.isEmpty()
            q.size()
        except NotImplementedError:
            raise unittest.SkipTest("Functions from the Queue ADT have not been implemented yet")
        except:
            self.fail("Missing functions from the Queue ADT")

    @skip_when_not_implemented
    def test_isEmpty(self):
        '''P1: Testing the isEmpty() method in QueueFE'''
        q = QueueFE()
        self.assertTrue(q.isEmpty(), "New queue is not empty")

        q.enqueue( 1 )
        self.assertFalse(q.isEmpty(), "Queue after an enqueue should not be empty")

        q.dequeue()
        self.assertTrue(q.isEmpty(), "Queue after the final dequeue should be empty")

    @skip_when_not_implemented
    def test_size(self):
        '''P1: Testing the size() method in QueueFE'''
        q = QueueFE()
        self.assertEqual(0, q.size(), "Empty queue has non-zero size")

        q.enqueue( 1 )
        q.enqueue( 2 )
        self.assertEqual(2, q.size(), "Incorrect size after enqueue")

        q.dequeue()
        self.assertEqual(1, q.size(), "Incorrect size after dequeue")

    @skip_when_not_implemented
    def test_dequeueOrder(self):
        '''P1: Testing the dequeue order in QueueFE'''
        q = QueueFE()

        q.enqueue( 1 )
        q.enqueue( 2 )
        q.enqueue( 3 )

        self.assertEqual(1, q.dequeue(), "The first item enqueued was not the first item dequeued")

    @skip_when_not_implemented
    def test_item_order(self):
        '''P1: Testing whether QueueFE preserves the order of all elements'''
        items = [1,2,3,4,5]

        q = QueueFE()
        for item in items:
            q.enqueue(item)

        dequeued_items = []
        while q.size() > 0:
            dequeued_items.append( q.dequeue() )

        self.assertEqual(items, dequeued_items, "Incorrect order of dequeued items")

    @skip_when_not_implemented
    def test_enqueue_speed(self):
        '''P1: Testing to make sure that QueueFE has a fast enqueue'''
        # Some quick calls to trigger NotImplementedError in case we're not ready to test yet
        q = QueueFE()
        q.enqueue( 1 )
        q.dequeue()

        list_timer = timeit.Timer("l.insert( 0, 1 )", "l = []")
        list_duration = min(list_timer.repeat(3, number=50*1000))

        queue_timer = timeit.Timer("q.enqueue( 1 )", "from hw2 import QueueFE; q = QueueFE()")
        queue_duration = min(queue_timer.repeat(3, number=50*1000))

        self.assertLess(queue_duration * 10, list_duration, "Fast Enqueue should be faster than prepending to a list")

class TestProblem2(unittest.TestCase):

    def test_API(self):
        '''P2: Sanity Test: Testing the presense of all methods in the Stack Abstract Data Type'''
        try:
            stack = Stack()
            stack.push(1)
            stack.push(2)
            stack.pop()
            stack.size()
            stack.isEmpty()
        except NotImplementedError:
            raise unittest.SkipTest("Functions from the Stack ADT have not been implemented yet")
        except:
            self.fail("Missing functions from the Stack ADT")

    @skip_when_not_implemented
    def test_isEmpty(self):
        '''P2: Testing the isEmpty() method in Stack'''
        stack = Stack()

        self.assertTrue(stack.isEmpty(), "New stack is not empty")

        stack.push( 1 )
        self.assertFalse(stack.isEmpty(), "Stack after a push should not be empty")

        stack.pop()
        self.assertTrue(stack.isEmpty(), "Stack after the final pop should be empty")

    @skip_when_not_implemented
    def test_size(self):
        '''P2: Testing the size() method in Stack'''
        stack = Stack()

        self.assertEqual(0, stack.size(), "Empty stack has non-zero size")

        stack.push( 1 )
        stack.push( 2 )
        self.assertEqual(2, stack.size(), "Incorrect size after push")

        stack.pop()
        self.assertEqual(1, stack.size(), "Incorrect size after pop")

    @skip_when_not_implemented
    def test_peek(self):
        '''P2: Testing the peek() method in Stack'''
        stack = Stack()

        stack.push( 1 )
        stack.push( 2 )
        self.assertEqual(2, stack.peek(), "Peek does not return most-recently added item")
        self.assertEqual(2, stack.peek(), "Peek should not remove the item from the stack")

        stack.pop()
        self.assertEqual(1, stack.peek(), "Peek does not show correct element after pop")

    @skip_when_not_implemented
    def test_popOrder(self):
        '''P2: Testing the pop order in Stack'''
        stack = Stack()

        stack.push( 1 )
        stack.push( 2 )
        stack.push( 3 )

        self.assertEqual(3, stack.pop(), "Pop did not return the most-recently-pushed item")

    @skip_when_not_implemented
    def test_item_order(self):
        '''P2: Testing to ensure that the Stack properly reverses the order of pushed items.'''
        items = [1,2,3,4,5]

        stack = Stack()
        for item in items:
            stack.push(item)

        reversed_items = items[::-1]
        popped_items = []
        while stack.size() > 0:
            popped_items.append( stack.pop() )

        self.assertEqual(reversed_items, popped_items, "Incorrect order of popped items")


class TestProblem3(unittest.TestCase):

    def test_API(self):
        '''P3: Sanity Test: Testing the presense of all methods in the Queue Abstract Data Type'''
        try:
            q = Queue()
            q.enqueue(1)
            q.enqueue(2)
            q.dequeue()
            q.isEmpty()
            q.size()
        except NotImplementedError:
            raise unittest.SkipTest("Functions from the Queue ADT have not been implemented yet")
        except:
            self.fail("Missing functions from the Queue ADT")

    @skip_when_not_implemented
    def test_isEmpty(self):
        '''P3: Testing the isEmpty() method in Queue'''
        q = Queue()
        self.assertTrue(q.isEmpty(), "New queue is not empty")

        q.enqueue( 1 )
        self.assertFalse(q.isEmpty(), "Queue after an enqueue should not be empty")

        q.dequeue()
        self.assertTrue(q.isEmpty(), "Queue after the final dequeue should be empty")

    @skip_when_not_implemented
    def test_size(self):
        '''P3: Testing the size() method in Stack'''
        q = Queue()
        self.assertEqual(0, q.size(), "Empty queue has non-zero size")

        q.enqueue( 1 )
        q.enqueue( 2 )
        self.assertEqual(2, q.size(), "Incorrect size after enqueue")

        q.dequeue()
        self.assertEqual(1, q.size(), "Incorrect size after dequeue")

    @skip_when_not_implemented
    def test_dequeueOrder(self):
        '''P3: Testing the dequeue order in Queue'''
        q = QueueFE()

        q.enqueue( 1 )
        q.enqueue( 2 )
        q.enqueue( 3 )

        self.assertEqual(1, q.dequeue(), "The first item enqueued was not the first item dequeued")

    @skip_when_not_implemented
    def test_item_order(self):
        '''P3: Testing whether QueueFE preserves the order of all elements'''
        items = [1,2,3,4,5]

        q = Queue()
        for item in items:
            q.enqueue(item)

        dequeued_items = []
        while q.size() > 0:
            dequeued_items.append( q.dequeue() )

        self.assertEqual(items, dequeued_items, "Incorrect order of dequeued items")


class TestProblem4(unittest.TestCase):

    def test_API(self):
        '''P4: Sanity Test: Testing the presense of all methods in the Deque Abstract Data Type'''
        try:
            dq = Deque()
            dq.addFront(1)
            dq.addRear(2)
            dq.removeFront()
            dq.removeRear()
            dq.isEmpty()
            dq.size()
        except NotImplementedError:
            raise unittest.SkipTest("Functions from the Deque ADT have not been implemented yet")
        except:
            self.fail("Missing functions from the Deque ADT")

    @skip_when_not_implemented
    def test_isEmpty(self):
        '''P4: Testing the isEmpty() method in Deque'''
        dq = Deque()
        self.assertTrue(dq.isEmpty(), "New deque is not empty")

        dq.addFront( 1 )
        self.assertFalse(dq.isEmpty(), "Queue after an addFront should not be empty")

        dq.removeFront()
        self.assertTrue(dq.isEmpty(), "Queue after the final removeFront should be empty")

        dq.addRear( 1 )
        self.assertFalse(dq.isEmpty(), "Queue after an addRear should not be empty")

        dq.removeRear()
        self.assertTrue(dq.isEmpty(), "Queue after the final removeRear should be empty")

    @skip_when_not_implemented
    def test_size(self):
        '''P4: Testing the size() method in Deque'''
        dq = Deque()
        self.assertEqual(0, dq.size(), "Empty queue has non-zero size")

        dq.addFront( 1 )
        dq.addFront( 2 )
        self.assertEqual(2, dq.size(), "Incorrect size after addFront")

        dq.removeFront()
        self.assertEqual(1, dq.size(), "Incorrect size after removeFront")

        dq.addRear( 3 )
        dq.addRear( 4 )
        self.assertEqual(3, dq.size(), "Incorrect size after addRear")

        dq.removeRear()
        self.assertEqual(2, dq.size(), "Incorrect size after removeRear")

    @skip_when_not_implemented
    def test_itemOrder(self):
        '''P4: Testing whether removeFront and removeRear preserve the order of all elements'''
        dq = Deque()

        dq.addFront( 3 )
        dq.addFront( 2 )
        dq.addFront( 1 )
        dq.addRear( 4 )
        dq.addRear( 5 )
        dq.addRear( 6 )

        front_removal = []
        while dq.size() > 0:
            front_removal.append( dq.removeFront() )

        self.assertEqual([1,2,3,4,5,6], front_removal, "Incorrect order of items returned by removeFront")

        dq.addFront( 3 )
        dq.addFront( 2 )
        dq.addFront( 1 )
        dq.addRear( 4 )
        dq.addRear( 5 )
        dq.addRear( 6 )

        rear_removal = []
        while dq.size() > 0:
            rear_removal.append( dq.removeRear() )

        self.assertEqual([6,5,4,3,2,1], rear_removal, "Incorrect order of items returned by removeRear")

class TestProblem5(unittest.TestCase):

    def test_API(self):
        '''P5: Sanity Test: Testing to make sure removeMin has been implemented in UnorderedList'''
        try:
            ul = UnorderedList()
            ul.add(3)
            ul.add(1)
            ul.add(2)
            ul.removeMin()
        except NotImplementedError:
            raise unittest.SkipTest("removeMin() has not been implemented yet")
        except:
            self.fail("Error when trying to call removeMin()")

    @skip_when_not_implemented
    def test_removeMin(self):
        '''P5: Does removeMin() return and remove the smallest item in the list?'''
        ul = UnorderedList()
        ul.add(3)
        ul.add(1)
        ul.add(2)

        self.assertEqual(1, ul.removeMin(), "Minimal item not returned from list")
        self.assertFalse(ul.search(1), "Minimal item not removed from list after being returned")

    @skip_when_not_implemented
    def test_asSort(self):
        '''P5: Implementing Selection Sort with removeMin'''
        ul = UnorderedList()

        # Using the removeMin functionality of UnorderedList to implement Selection Sort

        items = list(range(1000))
        random.shuffle(items)

        def isSorted(sequence):
            for i in range(len(sequence)-1):
                if sequence[i] > sequence[i+1]:
                    return False
            return True

        # Not self.assert, because we want this to be a harness error, not a test failure
        assert not isSorted(items)

        for item in items:
            ul.add(item)

        sorted_items = []
        while ul.size() > 0:
            sorted_items.append( ul.removeMin() )

        self.assertTrue(isSorted(sorted_items), "Items were not removed by removeMin in smallest-to-largest order")

if __name__ == "__main__":
    try:
        from hw2 import QueueFE
        from hw2 import Stack
        from hw2 import Queue
        from hw2 import Deque

        from UnorderedList import UnorderedList

        unittest.main(exit=False, verbosity=2)
    except ModuleNotFoundError:
        print("Unable to import functions or classes from hw2.py. Please ensure that hw2.py is located in the same directory as this test file, and that all classes and functions are named correctly.")
    except:
        import traceback
        traceback.print_exc()
    input("Press ENTER to dismiss...")
