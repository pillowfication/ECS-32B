class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

# API defined here: http://interactivepython.org/courselib/static/pythonds/BasicDS/TheUnorderedListAbstractDataType.html
class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def index(self, item):
        current = self.head

        idx = 0
        while current != None:
            if current.getData() == item:
                return idx
            else:
                current = current.getNext()
            idx += 1

        raise ValueError("%r is not in unordered list" % item)


    def insert(self, pos, item):
        node = Node(item)

        if pos == 0:
            node.setNext(self.head)
            self.head = node
        else:
            index = 0
            previous, current = None, self.head

            while index < pos:
                index += 1
                previous, current = current, current.getNext()
                if current is None and index < pos:
                    raise IndexError("unordered list assignment index out of range")

            node.setNext(current)
            previous.setNext(node)

    def pop(self, pos):
        if self.head is None:
            raise IndexError("pop from empty unordered list")

        if pos == 0:
            item = self.head.getData()
            self.head = self.head.getNext()
            return item

        previous, current = None, self.head
        index = 0

        while index < pos:
            previous, current = current, current.getNext()
            index += 1

        previous.setNext(current.getNext())
        return current.getData()

    def append(self, item):
        if self.head is None:
            self.head = Node(item)
            return

        current, next = self.head, self.head.getNext()

        while next is not None:
            current, next = next, next.getNext()

        current.setNext(Node(item))

    # Problem 5
    def removeMin(self):
        raise NotImplementedError
