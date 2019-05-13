# Your name and email here
# Markus Tran
# mkhtran@ucdavis.edu

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.emptyslots = self.size

        # https://planetmath.org/goodhashtableprimes
        self.good_sizes = [11, 23, 53, 97, 193, 389, 769, 1543]

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
