#working with arrays 

class Array:
    def __init__(self, length):
        self.length = length
        self.items = [None] * length
        self.count = 0
    
    def print(self):
        for i in range(self.count):
            print(self.items[i])
    
    def insert(self, value):
        if self.count == self.length:
            self.length = (self.length + round(self.length * .5))
            newArray = [None] * self.length
            for i in range(self.count):
                newArray[i] = self.items[i]
            self.items = newArray
            print("new array initialised")
            self.items[self.count] = value
            self.count += 1
            
        else:
            self.items[self.count] = value
            self.count += 1
    def lookupbyIndex(self,index):
        """index: provide index of item to lookup in array"""

        if index < 0 or index >= self.count:
            raise Exception("Index out of bounds")
        return self.items[index]
    

    def removeAt(self, index):
        if index < 0 or index >= self.count:
            raise Exception("Index out of bounds")
        for i in range(index, self.count - 1):
            self.items[i] = self.items[i + 1]
        self.items[self.count - 1] = None
        self.count -= 1
        
array = Array(5) #Creates an array of length 5
array.insert(1) #Inserts 1 into the array
array.insert(2) #Inserts 2 into the array
array.insert(3) #Inserts 3 into the array
array.insert(4) #Inserts 4 into the array
array.insert(5) #Inserts 5 into the array
array.insert(6) #Inserts 6 into the array, resizes the array
array.insert(7) #Inserts 7 into the array
# array.insert(8)
array.removeAt(3) #Removes the element at index 3

array.print() #Prints the array
print(array.lookupbyIndex(5))