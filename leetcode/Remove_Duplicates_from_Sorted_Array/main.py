#!/usr/bin/env python3
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    temp = [nums[0]]
    for idx, val in enumerate(nums[1:], 1):
        # print(f"prev: {nums[idx-1]}, cur: {val}")
        if nums[idx-1] != val:
            temp.append(val)
    nums[:] = temp
    return len(nums)

    

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        for num in f.readlines():
            n = list(map(int, (num.rstrip().split())))
            print(f"before: {n}")
            print(removeDuplicates(n))
            print(f"after: {n}")
            print("-------------")
