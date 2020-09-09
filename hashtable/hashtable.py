class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.bucket = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.bucket)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # load factor = # items / # total slots
        return self.count / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        prime = 1099511628211
        hash = 14695981039346656037

        for char in key:
            hash = hash * prime
            hash = hash ^ ord(char)

        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for char in key:
            hash = (hash * 33) + ord(char)

        return hash & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Day 1
        # index = self.hash_index(key)
        # self.bucket[index] = value

        # Day 2
        index = self.hash_index(key)
        new_node = HashTableEntry(key, value)
        cur_node = self.bucket[index]

        if self.bucket[index] == None:
            self.bucket[index] = new_node
            self.count += 1

        elif self.bucket[index] is not None and self.bucket[index].key == key:
            self.bucket[index].value = value

        elif self.bucket[index] is not None:
            while cur_node is not None:
                if cur_node.next is None:
                    cur_node.next = new_node
                    self.count += 1
                    return cur_node

                elif cur_node.next is not None and cur_node.next.key == key:
                    cur_node.next.value = value
                    return cur_node.next

                else:
                    cur_node = cur_node.next

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # Day 1
        # index = self.hash_index(key)
        #self.bucket[index] = None

        # Day 2
        index = self.hash_index(key)
        is_node = True
        cur_node = self.bucket[index]
        prev_node = None

        while cur_node is not None:
            if cur_node.key == key:
                if is_node:
                    if cur_node.next == None:
                        self.bucket[index] = None
                        cur_node = None
                    else:
                        self.bucket[index] = cur_node.next
                        cur_node = None
                else:
                    if cur_node.next == None:
                        prev_node.next = None
                        cur_node = None
                    else:
                        prev_node.next = cur_node.next
                        cur_node = None
                return

            is_node = False

            if cur_node.next == None:
                return

            prev_node = cur_node
            cur_node = cur_node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # Day 1
        # index = self.hash_index(key)
        # return self.bucket[index]

        # Day 2
        index = self.hash_index(key)
        cur_node = self.bucket[index]

        if cur_node is not None and cur_node.key == key:
            return cur_node.value
        else:
            while cur_node is not None:
                if cur_node.key == key:
                    return cur_node.value

                cur_node = cur_node.next

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_bucket = [None] * new_capacity
        cur_bucket = self.bucket
        self.bucket = new_bucket
        self.count = 0
        self.capacity = new_capacity
        index = 0

        while index < len(cur_bucket):
            cur_node = cur_bucket[index]

            if cur_node is not None:
                next_node = cur_node.next
                cur_node.next = None
                self.put(cur_node.key, cur_node.value)
                cur_bucket[index] = next_node

            elif cur_node is None:
                index += 1


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
