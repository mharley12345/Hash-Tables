class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            # TODO: increase size
            print("ERROR: Array is full")
            return

        if index >= self.count:
            # TODO: better error handling
            print("Error: Index out of bounds")
            return

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        if self.count == self.capacity:
            # TODO: increase size
            print("ERROR: Array is full")
            return

        # self.count += 1
        # self.storage[self.count - 1] = value

        self.storage[self.count] = value
        self.count += 1
        
    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage
        


    