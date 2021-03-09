# Print in Reverse

## Problem
Given a pointer to the head of a singly linked list, print each ***data*** values from the reversed list. If the given list is empty, do not print anything.

### Example

*head* refers to the linked list with ***data*** values 1 -> 2 -> 3 -> *NULL*

Print the following:
```
3
2
1
```

### Function  Parameters 

- *SinglyLinkedListNode* pointer head:  a reference to the head of the list

### Prints

The ***data*** values of each node in the reversed list.

### constraints 

- 1<= n<=1000
- 1 <= *list[i]*<= 1000, where *list[i]* is the *i^{th}* element of the linked list.
- 
### Sample input
```
3
5
16
12
4
2
5
3
7
3
9
5
5
1
18
3
13
```

### Sample Output
```
5
2
4
12
16
9
3
7
13
3
18
1
5
```
### Explanation

There are three test cases. The are no blank lines between test case output.
The first linked elements list has **5** elements: 16 -> 12 -> 4 -> 2 -> 5. Pointing this in reverse order produces:
```
5
2
4
12
16
```
The second linked list has 3 elements: 7 -> 3 -> 9 -> *NULL* Printing this in reverse order produces:
```
9
3
7
```

The third linked list has 5 elements: 5 -> 1 -> 18 -> 3 -> 13 -> *NULL*
```
13
3
18
1
5
```
