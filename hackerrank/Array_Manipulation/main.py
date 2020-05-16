#!/usr/bin/env python3

import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    arr = [0] * (n+1) # index starting with 1
    result = 0
    for a,b,k in queries:
        arr[a] += k
        if b+1 <= n:
            arr[b+1] -= k
    x = 0
    for _, val in enumerate(arr):
        x = x + val
        result = max(result, x)
        
    return result

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0]) # number of elements in the array

    m = int(nm[1]) # number of query

    queries = []

    for _ in range(m):
        queries.append(list(map(int, sys.stdin.readline().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)