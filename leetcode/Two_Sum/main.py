#!/usr/bin/env python3
from typing import List

def twoSum(nums: List[int], target:int) -> List[int]:
    value_index = {}
    index_target_diff = {}

    # O(n)
    for idx, val in enumerate(nums):
        value_index[val] = idx
        index_target_diff[idx] = target - val

    # O(n)
    for key, val in index_target_diff.items():
        # O(1)
        if value_index.get(val) and key != value_index.get(val):
            return [key, value_index[val]]
    
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        target = int(f.readline())
        nums = list(map(int, list(f.readline().rstrip().split())))
    
    result = twoSum(nums, target)
    print(result)