#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    if a[0]>b[0]:
        alice+=1
    elif a[0]<b[0]:
        bob+=1
    if a[1]>b[1]:
        alice+=1
    elif a[1]<b[1]:
        bob+=1
    if a[2]>b[2]:
        alice+=1
    elif a[2]<b[2]:
        bob+=1
    arr = []
    arr.append(alice)
    arr.append(bob)
    return arr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
