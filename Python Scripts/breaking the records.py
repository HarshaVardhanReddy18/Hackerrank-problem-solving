#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    m = scores[0]
    k = scores[0]
    icount = 0
    dcount = 0
    for i in range(len(scores)):
        if m<scores[i]:
            m = scores[i]
            icount+=1
        if k>scores[i]:
            k = scores[i]
            dcount+=1
    return (icount,dcount)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
