from UnorderedList import UnorderedList

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
        self.ulist = UnorderedList()

     def isEmpty(self):
        return self.ulist.size() == 0

     def push(self, item):
        self.ulist.append(item)

     def pop(self):
        # Note: UnorderedList.pop() is not implemented (https://piazza.com/class/jtqbsk4spmk58r?cid=70)
        return self.ulist.pop(self.ulist.size() - 1)

     def peek(self):
        # Note: UnorderedList.pop() is not implemented (https://piazza.com/class/jtqbsk4spmk58r?cid=70)
        item = self.ulist.pop(self.ulist.size() - 1)
        self.ulist.append(item)
        return item

     def size(self):
        return self.ulist.size()

# Problem 3

class Queue:
    def __init__(self):
        self.ulist = UnorderedList()

    def isEmpty(self):
        return self.ulist.size() == 0

    def enqueue(self, item):
        self.ulist.append(item)

    def dequeue(self):
        return self.ulist.pop(0)

    def size(self):
        return self.ulist.size()

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
