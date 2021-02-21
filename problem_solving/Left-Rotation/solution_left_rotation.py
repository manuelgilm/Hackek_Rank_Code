import random 
import argparse

random.seed(1994)
parser = argparse.ArgumentParser()
parser.add_argument("-n",help="Array dimension", type=int)
parser.add_argument("-d",help="Number of rotations to the left", type=int)



def rotateLeft(d, arr):
    arr_ = arr.copy()
    [arr_.insert(len(arr_),arr_.pop(0)) for _ in range(d)]
    return arr_

if __name__ == '__main__':
    args = parser.parse_args()


    arr = [random.randint(0,100) for _ in range(args.n)]
    arr_rotated = rotateLeft(args.d,arr)

    print(f"Arr is        : {arr}")
    print(f"Arr rotated is: {arr_rotated}")





    