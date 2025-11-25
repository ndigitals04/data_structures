from arrays import Array
from linkedlist import LinkedList
class Stack():
    def __init__(self):
        self.items = Array(25)
        self.min = LinkedList()


    def isEmpty(self):
        if self.items.count == 0:
            return True
        else:
            return False
    
    def push(self,item):
        if self.items.count == 0:
            self.min.addFirst(item)
        else:
            if item < self.min.tail:
                self.min.addLast(item)
                
        self.items.insert(item)
            
    
    def pop(self):
        if self.isEmpty():
            return "empty stack"
        else:
            popped_item = self.items[self.items.count -1]
            if popped_item == self.min.tail:
                self.min.deleteLast()
            self.items.removeAt(self.items.count -1)
            return popped_item
    
    def peek(self):
        if self.isEmpty():
            return "empty stack"
        else:
            return self.items[self.items.count - 1]
    
    def getMin(self):
        if self.isEmpty():
            return Exception("Stack is empty")
        return self.min.tail
    
    def __str__(self):
        return self.items.__str__()

class MinNode():
    def __init__(self):
        self.value = ""
        self.next = None
    
text = "abcd"
def reverseText(text):
    stack = Stack()
    if text == None:
        raise TypeError("Nonetype is not String")
    for item in text:
        stack.push(item)
    reversed_text = ""
    for item in range(len(text)):
        reversed_text += stack.pop()

    print(reversed_text)

stack = Stack()
stack.pop()
print(stack.peek())
print(stack.isEmpty())
print(stack)
stack.push(7)
stack.push(5)
stack.push(3)
stack.push(2)
stack.push(4)
stack.push(1)
print(stack.getMin())
stack.pop()
print(stack.getMin())
stack.pop()
print(stack.getMin())
stack.pop()
print(stack.getMin())

def check_if_expression_is_balanced(string):
    stack = Stack()
    brackets = {"(": ")", "<":">", "[":"]","{":"}"}
    balanced = False
    for char in string:
        if char == "(" or char =="<" or char == "[" or char =="{":
            stack.push(char)
        elif char == ")" or char == ">" or char== "]" or char == "}":
            popped_character = stack.pop()
            if brackets.get(popped_character,"empty") == char:
                balanced = True
            else:
                return False
    if stack.isEmpty():
        if balanced:
            return balanced
    else:
        return False

# expression = ")<<1>,34<5,3344>[4534343]({34423}) + 234> (<0>)"
# print(check_if_expression_is_balanced(expression))