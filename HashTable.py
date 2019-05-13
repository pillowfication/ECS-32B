# Your name and email here
# Markus Tran
# mkhtran@ucdavis.edu

foundPrimes = [2, 3]
def findNextPrime():
    check = foundPrimes[-1] + 2
    def isPrime(n):
        for prime in foundPrimes:
            if n % prime == 0:
                return False
        return True
    while not isPrime(check):
        check += 2
    foundPrimes.append(check)

good_sizes = [11, 23, 53, 97, 193, 389, 769, 1543]

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.emptyslots = self.size

        # https://planetmath.org/goodhashtableprimes
        self.good_sizes = good_sizes

    def getNextGoodSize(self):
        # Find the first valid good size
        for size in self.good_sizes:
            if size > self.size:
                return size

        # Otherwise, find the first prime number that is at least twice the current size
        # and add that value to the list of known good sizes.
        size = foundPrimes[-1]
        while size < self.size * 2:
            findNextPrime()
            size = foundPrimes[-1]

        good_sizes.append(size)
        return size

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    # Problem 3 Part 1
    def empty_slots(self):
        return self.emptyslots

    # Problem 3 Part 2
    def put(self, key, data):
        if self.empty_slots() == 0:
            # Rehash
            newSize = self.getNextGoodSize()
            oldSlots = self.slots
            oldData = self.data
            self.size = newSize
            self.slots = [None] * self.size
            self.data = [None] * self.size
            self.emptyslots = self.size
            for index in range(0, len(oldSlots)):
                self.put(oldSlots[index], oldData[index])

        # This code has been condensed from its original implementation
        # to be easier to read
        hashvalue = self.hashfunction(key, len(self.slots))
        while self.slots[hashvalue] != None and self.slots[hashvalue] != key:
            hashvalue = self.rehash(hashvalue, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            self.emptyslots -= 1
        else:
            self.data[hashvalue] = data #replace
