class hashmap():
    """ A fixed-sized hashmap in Python with separate chaining for collision avoidance.
    To minimize collisions, the number of slots in the hashmap is the smallest power of two greater than prescribed size, plus one. 

    Unit tests - cmd line:
    python unittests.py

    Usage:
    import hashmap
    """
    def __init__(self, size):
        """Constructor for a fixed-size hashmap that utilizes separate chaining.
        
        Keyword arguments:
        size -- capacity of hashmap
        """
        if type(size) is not int:
            raise TypeError("Error @param size: Expected type int.")
        if size < 1:
            raise ValueError("Error @param size: Expected >= 1.")
        
        # Number of slots = smallest power of 2 greater than size, plus one, to minimize collisions
        self.slots = 1<<(size-1).bit_length() + 1
        self.hashmap = [[] for i in range(self.slots)]
        self.num_items = 0
        self.size = size

    def set(self, key, value):
        """Stores key/value pair in hashmap 

        Keyword arguments:
        key -- key of key/value pair
        value -- value of key/value pair

        Return:
        True on success of store.
        False on failure of store (capacity reached, or key not a string)
        """
        if self.num_items >= self.size:
            return False

        if type(key) is not str:
            return False

        slot = self.__getslot(key)
        for idx, (k, v) in enumerate(slot):
            if k == key:
                slot[idx] = (key, value)
                return True
        slot.append((key, value))
        self.num_items += 1
        return True

    def get(self, key):
        """Retrieve value of key/value pair given the key

        Keyword arguments:
        key -- key of key/value pair

        Return:
        Value of key/value pair, if exists in hashmap
        None, if key/value pair not found in hashmap
        """
        slot = self.__getslot(key)
        for (k, v) in slot:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Deletes value of key/value pair from hashmap

        Keyword arguments:
        key -- key of key/value pair

        Return:
        Deleted value, if key/value pair exists in hashmap
        None, if key/value pair not found in hashmap
        """
        slot = self.__getslot(key)
        for idx, (k, v) in enumerate(slot):
            if k == key:
                slot[idx] = (key, None)
                self.num_items -= 1
                return v
        return None

    def load(self):
        """Load factor of hashmap

        Keyword arguments:
        (none)

        Return:
        Load factor, of type float
        """
        return 1.0*self.num_items/self.size

    def __getslot(self, key):
        """[Private Method] Retrieve slot where key hashes to in separate-chained hashmap

        Keyword arguments:
        key -- key to be found

        Return:
        Slot where key hashes to, of type list
        """
        return self.hashmap[key.__hash__() % self.slots]

