#!/usr/bin/env python3

import os
import sys

def sockMerchant(n, ar):
    """
    n: number of socks
    ar: the colors of eash sock
    """
    result = 0
    ar.sort() # O(nlogn)
    cur_color = None
    pair = 0
    for color in ar: # O(n)
        if not cur_color:
            cur_color = color
            pair = 1
        else:
            if cur_color == color:
                pair += 1
                if pair == 2: 
                    result += 1
                    cur_color = None
                    pair = 0
            else:
                cur_color = color
                pair = 1
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        ar = list(map(int, f.readline().rstrip().split()))

    # n = int(input())
    # ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()