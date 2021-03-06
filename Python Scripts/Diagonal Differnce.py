#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
    dig = 0
    gid = 0
    for i in range(n):
        for j in range(n):
            if (i==j):
                dig += arr[i][j]
    
    j = n-1
    for i in range(n):
        gid+=arr[i][j]
        j-=1
    if(gid>dig):
        return (gid-dig)
    elif(dig>gid):
        return (dig-gid)
    else:
        return 0
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
