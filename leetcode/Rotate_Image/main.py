#!/usr/bin/env python3
from typing import List

class Solution:
    def resolve(self, matrix: List[List[int]]) -> None:
        """
        0,0 0,1 0,2  0,2 1,2 2,2  
        1,0 1,1 1,2  0,1 1,1 2,1
        2,0 2,1 2,2  0,0 1,0 2,0
        """
        matrix[:] = [x[::-1] for x in list(zip(*matrix))]
