class linkedList:
    def __init__(self):
        self.items = [[None,None]] * 5
        self.count = 0
        self.length = 5
        self.first = ""
        self.last = ""

    def increaseLength(self):
        self.length = self.length + (self.length * .5)
        newLinkedList = [[None,None]] * round(self.length)
        for i in range(self.count):
            newLinkedList[i]= self.items[i]
        self.items = newLinkedList
        return self.items
    
    def getFirst(self):
        return self.items[0][0]
    def getLast(self):
        return self.last[0]
    
    def addFirst(self,item):
        if self.count == self.length:
            self.increaseLength()
                    
        if self.count == 0:
            self.items[0] = [item, None]
            self.last = self.items[0]
            self.count += 1
        else:
            self.items[self.count] = self.items[0]
            self.items[0] = [item,self.count]
            self.count += 1

    def addLast(self,item):
        if self.count == self.length:
            self.increaseLength()
        if self.count == 0:
            self.addFirst(item)
        else:
            self.items[self.count] = [item,None]
            self.last[1] = self.count
            self.last = self.items[self.count]
            self.count += 1

    def deleteFirst(self):
        if self.count == 0:
            raise BaseException("Linkedlist is empty")
        if self.count == 1:
            self.items[0] = self.last = [None,None]
            self.count -= 1
        else:
            newFirstIndex = self.items[0][1]
            self.items[0] = self.items[newFirstIndex]
            self.items[newFirstIndex] = [None,None] #turn new head of list to None in previous location
            self.count -= 1

    def deleteLast(self):
        if self.count == 0:
            raise BaseException("LinkedList is empty")
        elif self.count == 1:
            self.items[0] = self.last = [None,None]
        else:
            nextIndex = self.items[0][1]
            currentIndex = 0
            while True:
                if self.last == self.items[nextIndex]:
                    self.items[currentIndex] = [self.items[currentIndex][0],None]
                    self.last = self.items[currentIndex]
                    self.items[nextIndex] = [None,None]
                    self.count -= 1
                    break
                else:
                    currentIndex = nextIndex
                    nextIndex = self.items[nextIndex][1]
            
    def indexOf(self,item):
        currentIndex = 0
        i= 0
        while i<self.count:
            if self.items[currentIndex][0] == item:
                return currentIndex
            else:
                if self.items[currentIndex][1] == None:
                    break
                currentIndex = self.items[currentIndex][1]
        return f"{item} not found"
    
    def contains(self,item):
        currentIndex = 0
        i = 0
        while i<self.count:
            if self.items[currentIndex][0] == item:
                return True
            else:
                if self.items[currentIndex][1] == None:
                    break
                currentIndex = self.items[currentIndex][1]
        return False
    
    def print(self):
        return self.items
        # linkedlist = "["
        # for i in range(self.count):
        #     linkedlist += str(self.items[i][0]) + ","
        # linkedlist += "]"
        # return linkedlist
#deleteFirst deletelast indexof contains
linkedlist = linkedList()
# linkedlist.deleteFirst()
linkedlist.addFirst(2)
linkedlist.deleteFirst()
linkedlist.addFirst(4)
linkedlist.addFirst(6)
linkedlist.addFirst(8)
linkedlist.addFirst(10)
linkedlist.addLast(15)
linkedlist.addFirst(12)
linkedlist.addLast(30)
linkedlist.deleteFirst()
linkedlist.deleteLast()
print(linkedlist.contains(6))
print(linkedlist.indexOf(9))
print(linkedlist.getFirst())
print(linkedlist.getLast())
print(linkedlist.print())

    
