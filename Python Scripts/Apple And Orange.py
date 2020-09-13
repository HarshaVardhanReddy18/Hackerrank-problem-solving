#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    for i in range(len(apples)):
        apples[i] = apples[i] + a
    for i in range(len(oranges)):
        oranges[i] = oranges[i] + b
    ac = 0
    oc = 0
    for i in apples:
        if i>=s and i<=t:
            ac+=1
    for i in oranges:
        if i>=s and i<=t:
            oc+=1
    print(ac)
    print(oc)
        
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
