#!/usr/bin/env python3

import os
import sys

def jumpingOnClouds(c):
    # 1: tunderheads, 2: cmulus
    result = [0] * len(c)
    for index, value in enumerate(c[::-1]): # o(n)
        if index == 0:
            result[index] = 0
        else:
            jump1 = result[index- 1] + 1 if index - 1 >=0 and value != 1 else sys.maxsize
            jump2 = result[index- 2] + 1 if index - 2 >=0 and value != 1 else sys.maxsize
            result[index] = min(jump1,jump2)
    return result[len(c) - 1]

if __name__ == '__main__':
    # n: number of clouds
    # c: array of clouds

    with open('input.txt', 'r') as f:
        n = int(f.readline())
        c = list(map(int, f.readline().rstrip().split()))
    
    result = jumpingOnClouds(c) # o(n)
    print(result)