#!/usr/bin/env python3
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    nums[:] = sorted(list(set(nums)))
    return len(nums)

    

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        for num in f.readlines():
            n = list(map(int, (num.rstrip().split())))
            print(f"before: {n}")
            print(removeDuplicates(n))
            print(f"after: {n}")
            print("-------------")
