# Introduction to Data structures with python
This repository contains codes implementing data structures and alogrithms in Python.

## Table of Content
[Arrays](#
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

