#!/usr/bin/env python3

from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # n >= m
    m, n = len(nums1), len(nums2)
    if n < m:
        nums1, nums2, m, n = nums2, nums1, n, m

    start, end, halflen = 0, m, (n+m+1)/2
    while(start <= end):
        i = int((start+end)/2)
        j = int(halflen)-i
        if i > 0 and nums1[i-1] > nums2[j]:
            # i is too small
            end = i - 1
        elif i < m and nums1[i] < nums2[j-1]:
            # i is too big
            start = i + 1
        else:
            # i is fit
            if i == 0:
                maxLeft = nums2[j-1]
            elif j == 0:
                maxLeft = nums1[i-1]
            else:
                maxLeft = max(nums1[i-1], nums2[j-1])
            
            if (m+n) % 2 == 1:
                # in case of odd
                return maxLeft
            else:
                # in case of odd
                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i], nums2[j])
            return (maxLeft + minRight) / 2

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        nums1 = list(map(int, f.readline().rstrip().split()))
        nums2 = list(map(int, f.readline().rstrip().split()))
        result = findMedianSortedArrays(nums1, nums2)
        print(result)
    
