#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    def calc(x, y):
        hourglass = 0
        for i in range(x, x+3):
            for j in range(y, y+3):
                hourglass += arr[i][j]
        return hourglass - arr[x+1][y] - arr[x+1][y+2]
    
    res = -10000000
    for i in range(4):
        for j in range(4):
            res = max(res, calc(i,j))
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
