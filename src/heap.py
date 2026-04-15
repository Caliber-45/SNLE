class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self.bubble_up(len(self.data) - 1)

    def extract_min(self):
        if self.is_empty():
            return None
        
        min_val = self.data[0]
        last_val = self.data.pop()
        
        if not self.is_empty():
            self.data[0] = last_val
            self.bubble_down(0)
            
        return min_val

    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def bubble_up(self, index):
        while index > 0:
            parent_idx = (index - 1) // 2
            # Compare by cost, assuming value is (cost, node)
            if self.data[index][0] < self.data[parent_idx][0]:
                self.data[index], self.data[parent_idx] = self.data[parent_idx], self.data[index]
                index = parent_idx
            else:
                break

    def bubble_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left][0] < self.data[smallest][0]:
                smallest = left
            if right < size and self.data[right][0] < self.data[smallest][0]:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break


class MaxHeap:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self.bubble_up(len(self.data) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
            
        max_val = self.data[0]
        last_val = self.data.pop()
        
        if not self.is_empty():
            self.data[0] = last_val
            self.bubble_down(0)
            
        return max_val

    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]
        
    def is_empty(self):
        return len(self.data) == 0

    def bubble_up(self, index):
        while index > 0:
            parent_idx = (index - 1) // 2
            # Compare by priority, assuming value is (priority, pkg_id)
            if self.data[index][0] > self.data[parent_idx][0]:
                self.data[index], self.data[parent_idx] = self.data[parent_idx], self.data[index]
                index = parent_idx
            else:
                break

    def bubble_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.data[left][0] > self.data[largest][0]:
                largest = left
            if right < size and self.data[right][0] > self.data[largest][0]:
                largest = right

            if largest != index:
                self.data[index], self.data[largest] = self.data[largest], self.data[index]
                index = largest
            else:
                break
