# Sparse Arrays

## Problem

There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

### Function Description
The function must return an array of integers representing the frequency of occurrence of each query string in strings.

### Parameters 

- string strings[n] : an array of strings to search
- string queries[q] : an array of query strings

### Returns 

- int[q] : an array of results for each query

### constraints 

1<= n<=1000
1<=q<=1000

### Sample input 
```
strings -> aba baba aba xzxb

queries -> aba xzxb ab
```
### Sample output
```
2
1
0
```

### Code example

```
>>python solution_sparse_arrays.py -s aba-baba-xzxb -q aba-xzxb-ab
[2, 1, 0]
```


