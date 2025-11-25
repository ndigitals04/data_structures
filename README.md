# Introduction to Data structures with python
This repository contains codes implementing data structures and alogrithms in Python.

## Table of Content
[Arrays](#arrays)  
[LinkedList](#linkedlist)
## 🧾How to use
- Fork this repo
- Clone your forked repo to your pc.
- Follow table of content in the repo to understand each code representaion of a data structure.

## 🛂Contribute
Encounterd a bug in any part of the code or you just want to make your own contribution to better an implementation of a data structure or add a new one altogether? 

If any of these categories is you please feel free to contribute.
Just ensure to make a standard pull request by:
- providing good information on the bug you're solving if there is one.
- If you are making an implementation more efficient, explain how you did that.
- If adding a new structure let us know what it is.


## Contact
I'm available on [X](https://x.com/Ndigitals001) and [LinkedIn](https://linkedin.com/in/peter--ndukwe) if you want to make inquiries or collab😏.

### Arrays
Arrays are data structures with fixed length for stroring a particular sequence of values. They are best for use when one knows the exact quantity of items needed. In the Array class within the `arrays.py` file various methods were implemented. They include:
- The __init__() magic method serving as an initialization method for creation of an  array. When the array is called for the first time ie `Array[3]` This method creates it with some important values. As seen in the example the Array class takes an argument representing it's length. So when called __init__ method creates the array in the length defined as argument. It creates three variables which becomes accesible throughout the class.
    - length: specifies the total length of an array.
    - items: This represents the items in the array:
    - count: This is the number of added items to the array.

    One might ask what is the difference between the length and count variable?
The difference is that count is the number of items that have been added in the array while length is the total size of the array unless extended. Example of an array with length 5 created with the Array class in this repo would look like this upon initialization: `[None,None,None,None,None]`

    As you can see the length of the array which is 5 is represented by 5 Nonetype items. So in this case the length is 5 and count is 0. If an item was added to the Array it would like this: 
`[10,None,None,None,None]`
Now the length still remains 5 but the count is 1,having an actual value of 10 in it.

- The print() method: This method was added to enable one print out the items currently in the array. It checks if the array is empty and prints an empty `[]` if so. If it's not empty it prints out all the items in the array as a string.

- The insert() method: This method adds a new item into the array. It works by first checking if the current items in the array is equal to it's length. If it is the array length is increases by 50%. This increment is done by copying all of the items in the current array into a new one of increased length by 50% of the old. After the new array has been created, the item to be added is then confirmed not to be of Nonetype. If it's not the new item is added as the latest index into the array and then the total count of items in the array is increased.
Insert example:
``` 
array = Array[3] # define array with length of 3
array.insert(1) # insert 1 into array
array.insert(2) # insert 2 into array
array.print() # print array
```

- The lookupbyIndex() method: This method finds the item stored in a particular index of an array. The index to be looked up is provided as an argument to the `lookupbyIndex` method like so:
```
array = Array(3) #Array is defined
array.insert(2) #Insert 2 into array
array.inser(4)
array.lookupbyIndex(1) #lookup item stored with index of 1
# 4 is retuned as result
```
Now how does it work exactly? Very simple actually. We just check if the index provided is not less than 0 and is not above the total number of items in the array currently. If it fulfills those conditions, then the array is simply indexed with the index value to get the actual item stored in that index.

- The removeAt() method: This method removes from an array the index passed passed to it as an argument.
```
array.removeAt(2) #Removes item at index 2 in array
```
The method works by first checking if the index is not out of range ie less than 0 or greater than total items currently in the array. Then the array identifies the item in the position of the provided index and reassigns it to the item of the next index(i+1). It does this till the second to the last count index of the array.
If we had an array with these items `[10,20,30,40,50,None,None]`.If we used performed `array.removeAt(2)`, after the above stated operation, it will now look like `[10,30,40,40,None,None]`
After that, it simply replaces the last copied item with a Nonetype value. The array would then look like this `[10,30,40,None,None,None]`. This is one way of removing an item from an array through it's index with python.
- The max() method: This returns the maximum value of integers in the array.
- The intersect() method: This takes in another array as argument and returns intersecting values between itself and the passed array.
- The reverse() method: This reverses the order of the array and returns it as a new array.
- The insertAt() method: This takes in the value to be inserted and the index to be inserted into. It inserts the value at the given index.
- The toString() method: This methods converts the Array object to a string format that can be called and printed in the terminal through the print statement.

### LinkedList
- __init__() method: This method initilializes a linkedlist with several attributes including a python list [] made of 5 Nonetype values, a count variable for storing the number of values in the linkedlist, a length variable for storing it's size, a first and last variable for storing the head and tail nodes respectively.
- getpreviousNode(): This method helps to find the node before the node passed as argument to it. It would be useful for deleting.
- addFirst(): This method takes a value as argument and adds it to the linkedlist as the first/head node.
- addLast(): This method takes a value as argument and adds it to the linkedlist as the last/tail node.
- deleteFirst(): This deletes the first/head node of the linkedlist.
- deleteLast(): This deletes the last/tail node of the linkedlist.
- indexOf(): This method returns the index of the value passed to it as argument.
- contains(): This checks if the value passed as argument is present in the linkedlist and returns True or False.
- reverse(): This reverses the order of the linkedlist. The linkedlist itself is reversed.
- getKthNodeFromLastNode(): This method checks the distance from the head node to the node provided as argument. It then checks the node at that same distance from the tail node and returns it.
- printMiddle(): This prints the middle of the middle node value of the linkedlist. If it's size is even, it prints the two nodes in between.
- hasLoop(): This checks if the linkedlist is circular in nature. That means it loops and has no end.

- Node Class: The entire linkedlist defined here was only possible through this Node class. It has a value and next attributes that are defined at initialization. So that way each node can store it's own value and the node address next to it ie `node.value = 2, node.next = Node()`


