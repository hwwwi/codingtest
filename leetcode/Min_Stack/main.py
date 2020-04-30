#!/usr/bin/env python3
from typing import List
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.len = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.len += 1

    def pop(self) -> None:
        self.stack.pop()
        self.len -= 1
        
    def top(self) -> int:
        print(self.len)
        return self.stack[self.len - 1]

    def getMin(self) -> int:
        return min(self.stack)


class Solution:
    def resolve(self, actions:List[str], items:List[int]) -> List[int]:

        result = []
        for idx, action in enumerate(actions):
            if action == "MinStack":
                stack = MinStack()
                result.append(None)
            elif action == "push":
                stack.push(items[idx])
                result.append(None)
            elif action == "pop":
                stack.pop()
                result.append(None)
            elif action == "top":
                result.append(stack.top())
            elif action == "getMin":
                result.append(stack.getMin())
        return result