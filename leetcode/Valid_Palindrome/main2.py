#!/usr/bin/env python3

class Solution:
    def resolve(self, s: str) -> bool:
        temp = []
        for char in s:
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9':
                temp.append(char.lower())
        return temp == temp[::-1]