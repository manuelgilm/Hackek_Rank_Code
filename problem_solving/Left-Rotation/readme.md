# Left Rotation

## Problem

A left rotation operation on an array of size **n** shifts each of the arrays elements 1 unit to the left. Given an integer, *d*, rotate the array that many steps left and return the result.

### Example

$d=2$
$arr=[1,2,3,4,5]$
After 2 rotations; $arr'=[3,4,5,1,2]$

### Function Description


_rotateLeft_  has the following parameters:

-   _int d:_  the amount to rotate by
-  n: array length
### Returns
- int[n]: the rotated array

### Constraints

- $1<=n<=10^5$
- $1<=d<= n$
- $1<=a[i]<= n$

### Sample input

 ```
5 4
1 2 3 4 5
```

### Sample Output 
```
5 1 2 3 4
```

### Code example
```

>>python solution_left_rotation.py -n 5 -d 4

Arr is        : [61, 57, 82, 37, 90]
Arr rotated is: [90, 61, 57, 82, 37]
```
