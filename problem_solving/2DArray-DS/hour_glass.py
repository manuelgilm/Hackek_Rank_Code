import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.

arr = [[random.randint(-9,9) for _ in range(6)] for _ in range(6)]

def hourglassSum(arr):
    
    sum_ = []
    for i in range(4):
        for m in range(4):
            a = [arr[n+i][m:m+3] if n != 1 else [0,arr[n+i][m+1],0] for n in range(3)]
            sum_.append(sum([e for el in a for e in el]))

    return max(sum_)
        

    
def show_2darray():
    print("----------------")
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()
    

if __name__ == '__main__':
    print("\n arr \n")
    [print(*row) for row in arr]
    print(f"\nThe maximum is: {hourglassSum(arr)}")
