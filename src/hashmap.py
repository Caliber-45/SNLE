class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class CustomHashMap:
    def __init__(self, size=11):
        self.size = size
        self.buckets = [None] * self.size
        self.count = 0

    def _hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def load_factor(self):
        return self.count / self.size

    def _insert_without_resize(self, key, value):
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return False
            current = current.next

        new_node = HashNode(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.count += 1
        return True

    def resize(self):
        old_buckets = self.buckets
        self.size = self.size * 2 + 1
        self.buckets = [None] * self.size
        old_count = self.count
        self.count = 0

        for head in old_buckets:
            current = head
            while current is not None:
                self._insert_without_resize(current.key, current.value)
                current = current.next

        self.count = old_count

    def put(self, key, value):
        inserted = self._insert_without_resize(key, value)
        if inserted and self.load_factor() > 0.7:
            self.resize()

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        previous = None

        while current is not None:
            if current.key == key:
                if previous is None:
                    self.buckets[index] = current.next
                else:
                    previous.next = current.next
                self.count -= 1
                return True
            previous = current
            current = current.next
        return False

    def contains(self, key):
        return self.get(key) is not None
