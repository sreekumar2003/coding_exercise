#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    bob = 0
    alice = 0
    result = []
    for i in range(0,3):
        if a[i]>b[i]:
            alice += 1
        elif a[i]<b[i]:
            bob += 1
    result.append(alice)
    result.append(bob)
    return result
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')




input
5 6 7
3 6 10

output
1 1

    fptr.close()
