from arrays import Array
class DoubleStack():
    def __init__(self,size):
        self.items = Array(size)
        self.highest_index1 = None
        self.highest_index2 = None

    def __isFull(self):
        if self.items.count == self.items.length:
            return True
        else:
            return False
    def isFull1(self):
        return self.__isFull()
    
    def isFull2(self):
        return self.__isFull()
    
    def isEmpty1(self):
        if self.highest_index1 == None:
            return True
        else:
            return False
    
    def isEmpty2(self):
        if self.highest_index2 == None:
            return True
        else:
            return False
        
    def push1(self,item):
        if self.__isFull():
            raise BaseException("Stack is Full")
        elif self.items.count == 0:
            self.items.insert(item)
            self.highest_index1 = 0
        elif self.items.count == 1 and self.highest_index2 == 0:
            self.items.insertAt(item,0)
            self.highest_index1 = 0
            self.highest_index2 = 1
        else:            
            print(self.items, "stack after loop")
            self.items.insertAt(item,self.highest_index1 + 1)
            self.highest_index2 += 1
            self.highest_index1 += 1
            
    def push2(self,item):
        if self.__isFull():
            raise BaseException("Stack is Full")
        elif self.items.count == 0:
            self.items.insert(item)
            self.highest_index2 = 0
        elif self.items.count == 1 and self.highest_index1 == 0:
            self.items.insertAt(item,1)
            self.highest_index2 = 1
        else:
            self.items.insert(item)
            self.highest_index2 += 1

    def peek1(self):
        if self.isEmpty1():
            return "Stack 1 is empty"
        return self.items[self.highest_index1]
    def peek2(self):
        if self.isEmpty2():
            return "Stack 2 is empty"
        return self.items[self.highest_index2]

    def pop1(self):
        if self.isEmpty1():
            return "Stack 1 is Empty, can't pop"
        popped_item = self.items[self.highest_index1]
        self.items.removeAt(self.highest_index1)
        if self.items.count != 0:
            self.highest_index1 -= 1
            self.highest_index2 -= 1
        else:
            self.highest_index1 = None
            self.highest_index2 = None
        return popped_item
    
    def pop2(self):
        if self.isEmpty2():
            return "Stack 2 is Empty, can't pop"
        popped_item = self.items[self.highest_index2]
        self.items.removeAt(self.highest_index2)
        self.highest_index2 -= 1
        return popped_item
      
    def __str__(self):
        return self.items.__str__()

stack = DoubleStack(7)
stack.push1(1)
stack.push2(2)
print("first_print", stack)
print("second_print", stack)
stack.push1(3)
print("third_print", stack)
stack.push1(3)
stack.push2(5)
stack.push2(6)
stack.push1(7)
print(stack.pop1())
print(stack.pop2())
print(stack.peek1())
print(stack.peek2())
stack.pop1()
stack.pop2()
stack.pop1()
stack.pop2()
stack.pop1()
stack.pop2()
print(stack.isEmpty1())
print(stack.isEmpty2())
print(stack.isFull1())
print(stack.isFull2())