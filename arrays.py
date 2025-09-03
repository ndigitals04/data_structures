#working with arrays 

class Array:
    def __init__(self, length):
        self.length = length
        self.items = [None] * length
        self.count = 0
    
    def print(self):
        if self.length == 0:
            print("[]")
        
        array_str = "["
        for i in range(self.count):
            if i == self.count - 1:
                array_str += str(self.items[i]) + "]"
            else:
                array_str+=  str(self.items[i]) +", "
        print(array_str)
    
    def insert(self, value):
        if self.count == self.length:
            self.length = (self.length + round(self.length * .5))
            newArray = [None] * self.length
            for i in range(self.count):
                newArray[i] = self.items[i]
            self.items = newArray
            
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

    def max(self):
        #run time complexity: O(n)
        if self.count == 0:
            raise Exception("Array is empty")
        max = 0
        for i in range(self.count):
            if self.items[i] > max:
                max = self.items[i]
        return max
    
    def intersect(self,array):
        """array: provide another array to find intersection with
        method returns a new array with the values intersecting"""
        if self.count == 0 or array.count == 0:
            raise Exception("One of the arrays is empty")
        elif self.count >= array.count:
            smaller_array = array.items
            smaller_count = array.count
            larger_array = self.items
        else:
            smaller_array = self.items
            larger_array = array.items

        intersection = Array(smaller_count) 
        for i in range(smaller_count):
            if smaller_array[i] in larger_array:
                intersection.insert(smaller_array[i])
        return intersection
        
    def reverse(self):
        """method reverses the array"""
        reversed_array = Array(self.length)
        count_from_end = self.count - 1
        for i in range(self.count):
            reversed_array.insert(self.items[count_from_end])
            count_from_end-= 1
        print(reversed_array.items)
        return reversed_array
    
array = Array(5) #Creates an array of length 5
array.insert(1) #Inserts 1 into the array
array.insert(2) #Inserts 2 into the array
array.insert(34) 
array.insert(3) #Inserts 3 into the array
array.insert(4) #Inserts 4 into the array
array.insert(5) #Inserts 5 into the array
array.insert(6) #Inserts 6 into the array, resizes the array
array.insert(7) #Inserts 7 into the array
# array.insert(8)
array.removeAt(3) #Removes the element at index 3

array.print() #Prints the array
print(array.lookupbyIndex(5)) # looksup item in array with index of 5
print(array.max()) # returns number with the largest value.
array2 = Array (3)
array2.insert(2)
array2.insert(3)
array2.insert(7)

intersection = array.intersect(array2) # returns intersection btw array and array2
intersection.print()
print(intersection.items)
reversed_array = array.reverse() # returns a new array with the values in reverse order
reversed_array.print()