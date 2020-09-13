#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    k = len(grades)
    c = []
    for i in range(k):
        if grades[i]<38:
            c.append(grades[i])
        elif grades[i]>38 and (grades[i])%5==0:
            c.append(grades[i])
        elif grades[i] >= 38 and (grades[i]) %5!=0:
            a = int(grades[i]/5)
            b = (a+1)*5
            if (b-grades[i])<3:
                c.append(b)
            else:
                c.append(grades[i])
    # Write your code here
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
