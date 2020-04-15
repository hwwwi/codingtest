#!/usr/bin/env python3

import os
import sys

def sockMerchant(n, ar):
    """
    n: number of socks
    ar: the colors of eash sock
    """
    result = 0
    socks_by_color = [0] * 101
    for color in ar:
        socks_by_color[color] += 1
    
    for amount in socks_by_color:
        result += int(amount/2)
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