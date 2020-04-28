#!/usr/bin/env python3

from typing import List

class Solution:
    def resolve(self,  numRows: int) -> List[List[int]]:
        result = []
        if not numRows:
            return result
        for i in range(1, numRows+1):
            row = []
            for j in range(1, i+1):
                # print(f"i:{i}, j:{j}, result: {result}")
                if j == 1 or j == i:
                    row.append(1)
                else:
                    row.append(result[i-2][j-2] + result[i-2][j-1])      
            result.append(row)
        return result
