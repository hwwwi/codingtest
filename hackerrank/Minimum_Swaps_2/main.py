#!/usr/bin/env python3

import sys

def solve(n, arr):
    count = 0
    for idx in range(n):
        while(idx != arr[idx]-1):
            #print(arr)
            arr[arr[idx]-1], arr[idx] = arr[idx], arr[arr[idx]-1] 
            count+=1
    return count

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    print (solve(n, arr))