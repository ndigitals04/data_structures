class LinkedList():
    def __init__(self):
        self.items = [None] * 5
        self.count = 0
        self.length = 5
        self.first = None
        self.last = None
    def getPreviousNode(self,node):
        current = self.first
        while current.next != node:
                current = current.next
        return current

    def addFirst(self,value):
        if self.count == 0:
            self.first = Node()
            self.first.value = value
            self.first.next = None
            self.last = self.first
            self.count += 1
        else:
            first_node = self.first
            self.first = Node()
            self.first.value = value
            self.first.next = first_node
            self.count += 1
    def addLast(self,value):
        if self.count == 0:
            self.addFirst(value)
        else:
            # previous_node = self.getPreviousNode(self.last)
            last_node = Node()
            self.last.next = last_node
            self.last = last_node
            self.last.value = value
            self.last.next = None
            self.count += 1

    def deleteFirst(self):
        if self.count == 0:
            return
        elif self.count == 1:
            self.first = self.last = None
            self.count -= 1
        else:
            first_node = self.first
            self.first = self.first.next
            del first_node
            self.count -= 1
    
    def deleteLast(self):
        if self.count == 0:
            return
        elif self.count == 1:
            self.first = self.last = None
            self.count -= 1
        else:
            previous_node = self.getPreviousNode(self.last)
            last_node = self.last
            self.last = previous_node
            self.last.next = None
            del last_node
            self.count -= 1

    def indexOf(self,value):
        currentIndex = 0
        if self.first == None:
            return f"{value} not found"
        node = self.first
        while node != None:
            if node.value == value:
                return currentIndex
            else:
                node = node.next
                currentIndex += 1
        return f"{value} not found"
        
    def contains(self,value):
        value_index = self.indexOf(value)
        if type(value_index) == int:
            return True
        else:
            # print(type(value_index), value_index)
            return False
    @property
    def size(self):
        return self.count
    @property
    def head(self):
        if (self.first) != None:
            return self.first.value
        else:
            return
    @property
    def tail(self):
        if self.last != None:
            return self.last.value
        else:
            return
        
    def reverse(self):
        if self.count == 0:
            return
        else:
            print(self.count)
            previous_node = self.first
            current_node = previous_node.next

            while current_node != None:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
        
            last_node = self.first
            last_node.next = None
            first_node = self.last
            self.last = last_node
            self.first = first_node

        return self
    
    def getKthNodeFromLastNode(self,k):
        if k > self.count:
            return f"k {k} is equal or greater than size of linkedlist"
        elif k <= 0:
            return "k can't be 0 or less than 0"
        else:
            start_node = self.first
            kth_node = self.first
            for i in range(1,k):
                kth_node = kth_node.next
            start_to_kth_node_distance = int(k) - 1 
            counter = 1
            while kth_node != self.last:
                kth_node = kth_node.next
                start_node = start_node.next
                counter += 1
            return start_node.value
        
    def printMiddle(self):
        count_node = self.first
        middle_node = self.first
        while count_node != self.last and count_node.next != self.last:
            count_node = count_node.next.next
            middle_node = middle_node.next
        if count_node == self.last:
            return middle_node.value
        else:
            return (middle_node.value,middle_node.next.value)
        # if self.count % 2 != 0: 
        #     count_node = self.first
        #     middle_node = self.first
        #     while count_node != self.last:
        #         count_node = count_node.next.next
        #         middle_node = middle_node.next
        #     return middle_node.value
        # else:
        #     count_node = self.first.next
        #     middle_node = self.first
        #     while count_node != self.last:
        #         count_node = count_node.next.next
        #         middle_node = middle_node.next 
        #     return (middle_node.value, middle_node.next.value)               
        
    def hasLoop(self):
        slow_node = self.first
        fast_node = self.first
        while fast_node.next != None:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

            if fast_node == slow_node:
                return True
        return False
    def __str__(self):
        if self.first == None:
            return "[]"
        current = self.first.next
        string_linkedlist = "[" + str(self.first.value)
        while current != None:
            string_linkedlist += "," + str(current.value)
            current = current.next
        string_linkedlist += "]"
        return string_linkedlist

class Node():
    def __init__(self):
        self.value = ""
        self.next = ""

linkedlist = LinkedList()
linkedlist.addFirst(4)
linkedlist.addLast(3)
linkedlist.addFirst(0)
linkedlist.addLast(5)
linkedlist.addFirst(8)
linkedlist.addLast(7)
linkedlist.addLast(90)
linkedlist.addLast(100)
linkedlist.addLast(110)
linkedlist.addFirst(7)
linkedlist.addFirst(5)
linkedlist.addFirst(6)
linkedlist.addFirst(45)
linkedlist.deleteFirst()
linkedlist.deleteLast()
print(linkedlist.indexOf(8))
print(linkedlist.contains(4))
print(linkedlist.size)
print(linkedlist.head)
print(linkedlist.tail)
print(linkedlist)
print(linkedlist.reverse())
print(linkedlist.getKthNodeFromLastNode(5))
print(linkedlist.printMiddle())
print(linkedlist.hasLoop())
# print(linkedlist.size)
# print(linkedlist.head)
# print(linkedlist.tail)