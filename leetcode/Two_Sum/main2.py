#!/usr/bin/env python3
from typing import List

def twoSum(nums: List[int], target:int) -> List[int]:
    # one-pass hashmap

    h = {}
    for idx, val in enumerate(nums):
        n = target - val
        if n in h:
            return [h[n], idx]    
        else:
            h[val] = idx
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        target = int(f.readline())
        nums = list(map(int, list(f.readline().rstrip().split())))
    
    result = twoSum(nums, target)
    print(result)