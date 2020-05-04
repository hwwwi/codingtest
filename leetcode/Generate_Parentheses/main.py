#!/usr/bin/env python3

from typing import List
from collections import deque

class Solution:
    def resolve(self, n: int) -> List[str]:
        def parentheses(cur: str) -> None:
            left = cur.count("(")
            right = cur.count(")")
            if left + right == 2*n and left == right:
                result.append(cur)
                return None
            if (left > n) or (right > n) or (right > left):
                return None
            parentheses(cur+"(")
            parentheses(cur+")")
        result = []
        parentheses("(")
        return result

