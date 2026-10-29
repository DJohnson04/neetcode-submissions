class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
            self.dynamicArray = [None] * capacity
            self.size = 0

    def get(self, i: int) -> int:
        return self.dynamicArray[i]

    def set(self, i: int, n: int) -> None:
        self.dynamicArray[i] = n

    def pushback(self, n: int) -> None:
        
        if self.size == self.capacity:
            self.resize()
        self.size += 1
        self.dynamicArray[self.size - 1] = n
        
    def popback(self) -> int:
        self.size -= 1
        return self.dynamicArray[self.size]

    def resize(self) -> None:
        print(self.dynamicArray)
        self.capacity *= 2
        old_elements = self.dynamicArray[:self.size]
        self.dynamicArray = [None] * self.capacity
        self.dynamicArray[:self.size] = old_elements

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity