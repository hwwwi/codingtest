#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # a: array
    # n: len of array
    # d: rotation
    global n
    rotate = d if n >= d else d - n
    # print(f"d: {d}, n:{n}, d-n:{d-n}")
    return a[rotate:] + a[0:rotate]
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
