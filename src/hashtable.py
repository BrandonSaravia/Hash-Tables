# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)

        return hash & 0xFFFFFFFF


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        
        index = self._hash_mod(key)

        current_node = self.storage[index]

        while current_node is not None and self.storage[index].key != key:
            last_pair = current_node
            current_node = last_pair.next

        if current_node is not None:
            current_node.value = value
        else:
            new_pair = LinkedPair(key,value)
            new_pair.next = self.storage[index]
            self.storage[index] = new_pair


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print("Warning: Key not found")
            return
        
        if self.storage[index].key == key:
            self.storage[index] = self.storage[index].next
        else:
            key_found = False
            previous_node = self.storage[index]
            current_node = self.storage[index].next
            while key_found == False:
                if current_node == None:
                    print("Warning: Key not found")
                    return
                if current_node.key == key:
                    found_key_value = current_node.value
                    previous_node.next = current_node.next
                    key_found = True
                    return found_key_value
                else:
                    previous_node = current_node
                    current_node = current_node.next




    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        current_node = self.storage[index]
        if current_node is None: 
            return None
        else:
            if current_node.key == key:
                return current_node.value
            else:
                current_node = current_node.next
                key_found = False
                while key_found == False:
                    if current_node == None:
                        return None
                    if current_node.key == key:
                        key_found = True
                        return current_node.value
                    else:
                        current_node = current_node.next

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2

        new_storage = [None] * self.capacity
        
        for pair in self.storage:
            if pair is not None:
                new_index = self._hash_mod(pair.key)
                new_storage[new_index] = pair

        self.storage = new_storage




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
