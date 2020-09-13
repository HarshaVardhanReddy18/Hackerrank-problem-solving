#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    k = len(arr)
    mins=maxs=0
    for i in range(k-1):
        mins+=arr[i]
    for i in range(1,k):
        maxs+=arr[i]

    print(mins,maxs)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
