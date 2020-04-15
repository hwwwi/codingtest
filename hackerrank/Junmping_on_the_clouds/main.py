#!/usr/bin/env python3

import os
import sys

def jumpingOnClouds(c, pos):
    # 1: tunderheads, 2: cmulus
    if pos == len(c) - 1:
        # reach to the end
        return 0
    if pos >= len(c) or c[pos] == 1:
        # over the border or tunderheads
        return sys.maxsize
    return min(jumpingOnClouds(c, pos + 1), jumpingOnClouds(c, pos + 2)) + 1

if __name__ == '__main__':
    # n: number of clouds
    # c: array of clouds

    with open('input.txt', 'r') as f:
        n = int(f.readline())
        c = list(map(int, f.readline().rstrip().split()))
    
    result = jumpingOnClouds(c, 0) # o(n)
    print(result)