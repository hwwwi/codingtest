#!/usr/bin/env python3
from typing import List

def twoSum(nums: List[int], target:int) -> List[int]:

    hashmap = {}
    for idx, val in enumerate(nums):
        n = target - val
        if n in hashmap:
            print(hashmap[n])
            return [hashmap[n] + 1, idx + 1]
        else:
            hashmap[val] = idx
    
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        target = int(f.readline())
        nums = list(map(int, list(f.readline().rstrip().split())))
    
    result = twoSum(nums, target)
    print(result)