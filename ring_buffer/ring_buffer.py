class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current_index = 0

    def append(self, item):
        if len(self.storage) >= self.capacity:
            # Overwrite oldest item
            self.storage[self.current_index] = item
            self.current_index = (self.current_index + 1) % self.capacity
        else:
            # Just append
            self.storage.append(item)

    def get(self):
        return self.storage

# A ring buffer is a non-growable buffer with a fixed size. 
# When the ring buffer is full and a new element is inserted, 
# the oldest element in the ring buffer is overwritten with the newest element. 
# This kind of data structure is very useful for use cases such as storing logs and history information, 
# where you typically want to store information up until it reaches a certain age, 
# after which you don't care about it anymore and don't mind seeing it overwritten by newer data.