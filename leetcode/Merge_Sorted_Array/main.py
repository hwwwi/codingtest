#!/usr/bin/env python3

from typing import List
class Solution:
    def resolve(self,  nums1: List[int], m: int, nums2: List[int], n: int) -> None:        
        temp = []
        idx1 = 0
        idx2 = 0

        nums1[:] = nums1[:m]
        while (idx2 < n and idx1 < m):
            val1 = nums1[idx1]
            val2 = nums2[idx2]
            if val1 == val2:
                temp.append(val1)
                temp.append(val2)
                idx1 += 1
                idx2 += 1
            elif val1 < val2:
                # print(f"val1 {idx1} {val1}")
                temp.append(val1)
                idx1 += 1
            else:
                #print(f"val2 {idx2} {val2}")
                temp.append(val2)
                idx2 += 1
        while(idx1 < m):
            temp.append(nums1[idx1])
            idx1 +=1
        while(idx2 < n):
            temp.append(nums2[idx2])
            idx2 += 1
        nums1[:] = temp + nums1[len(temp):]