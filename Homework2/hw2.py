
# Problem 1

class QueueFE:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        # Push the item to the end of the List, which is the tail of the Queue
        self.items.append(item)

    def dequeue(self):
        # Pop/Shift an item from the start of the List, which is the head of the Queue
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# Problem 2

class Stack:
     def __init__(self):
        raise NotImplementedError

     def isEmpty(self):
        raise NotImplementedError

     def push(self, item):
        raise NotImplementedError

     def pop(self):
        raise NotImplementedError

     def peek(self):
        raise NotImplementedError

     def size(self):
        raise NotImplementedError

# Problem 3

class Queue:
    def __init__(self):
        raise NotImplementedError

    def isEmpty(self):
        raise NotImplementedError

    def enqueue(self, item):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError

# Problem 4

class Deque:
    def __init__(self):
        raise NotImplementedError

    def isEmpty(self):
        raise NotImplementedError

    def addFront(self, item):
        raise NotImplementedError

    def addRear(self, item):
        raise NotImplementedError

    def removeFront(self):
        raise NotImplementedError

    def removeRear(self):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError
