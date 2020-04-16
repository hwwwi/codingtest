#!/usr/bin/env python3
import sys
import os

def countingValleys(n, s):
    # n: the number of steps Gary takes
    # s: a string describing his path

    result = 0
    sea_level = 1000000 # 10^6
    pos = sea_level # initial level
    status = 0 # initial status, 0 means not valley

    for step in list(s):
        # check action
        pos = pos + 1 if step == 'U' else pos - 1

        # calculate
        if pos >= sea_level:
            # in sea-level or mountain
            status = 0
        elif status != 1 and pos <= sea_level:
            # if previous status is not valley but current is
            status = 1
            result += 1
    return result

if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        n = int(f.readline())
        s = f.readline()

        result = countingValleys(n, s)
        print(result)