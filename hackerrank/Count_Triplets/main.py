#!/usr/bin/env python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    res = 0
    left = defaultdict(int)
    right = Counter(arr)

    for val in arr:
        right[val] -= 1 # remove current value from right
        if val % r == 0:
            if (val//r in left) and (val*r in right):
                res += (left[val//r] * right[val*r])
        left[val] += 1 # add current value to left
    return res
            
if __name__ == '__main__':
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    print(ans)