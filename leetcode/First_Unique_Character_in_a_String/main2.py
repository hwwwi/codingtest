#!/usr/bin/env python3

import collections

class Solution:
    def resolve(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for i in s:
            if count[i] == 1:
                return s.find(i) 
        return -1
 