# Insert a node at a specific position in a linked list

## Problem

Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integers as its ***data***  attribute, insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

### Example

*head* refers to the first node in the list 1 -> 2 -> 3
*data*=4
*position*=2

insert a node at position **2** with *data=* **4** . the new list is 1 -> 2 -> 4 -> 3

### Function  Parameters 

insertNodeAtPosition has the following parameters:

-   *head*: a SinglyLinkedListNode pointer to the head of the list
-   *data*: an integer value to insert as data in your new node
-   *position*: an integer position to insert the new node, zero based indexing

### constraints 

- 1<= n<=1000
- 1<= SinglyLinkedListNode[*i*].data<= 1000, where *SingleLinkedListNode[i]* is the i^{th} element of the linked list.
- 0<= *position*<= n

### Sample input
```
3
16
13
7
1
2
```

### Sample Output
```
16 13 1 7
```

### Explanation

The initial linked list is 16 -> 13 -> 7. insert 1 at the position 2 which currently has 7 in it. The updated linked list is 16 -> 13 -> 1 -> 7

