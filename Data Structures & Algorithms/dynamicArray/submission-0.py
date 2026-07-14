class DynamicArray:
    
    def __init__(self, capacity: int):
        
        self.size = 0
        self.capacity = capacity
        if capacity > 0:
            self.arr = [None] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        if self.size > 0:
            value = self.arr[self.size - 1]
            self.size -= 1
        return value
 

    def resize(self) -> None:
        new_list = [None] * (len(self.arr) * 2)
        for i in range(self.size):
            new_list[i] = self.arr[i]
            
        self.arr = new_list
        self.capacity = len(self.arr)


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
