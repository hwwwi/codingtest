#!/usr/bin/env python3

import sys

def solve(t, n):
    # One person bribe at most two people
    # minimum number of bribes to get the queue into the current state
    # print 'Too chaotic', if is not possible
    count = [0] * t

    check = True
    for i in range(t)[::-1]:
        if check:
            check = False
            for j in range(i):
                #print(f"count: {count}, n: {n}")
                if (n[j] > n[j+1]):
                    count[n[j]-1] += 1
                    if count[n[j]-1] > 2:
                        print("Too chaotic")
                        return
                    check = True
                    n[j], n[j+1] = n[j+1], n[j]
    print(sum(count))

if __name__ == '__main__':
    # first line: number of testcase
    # t: number of people in the queue
    # n: final state of the queue

    tc = int(input())
    for _ in range(tc):
        t = int(sys.stdin.readline())
        n = list(map(int, sys.stdin.readline().rstrip().split()))
        solve(t, n)