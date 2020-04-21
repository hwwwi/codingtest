#!/usr/bin/env python3

from typing import List
def longestCommonPrefix(strs:List[str]) -> str:
    
    prefix = ""

    for word in zip(*strs):
        if len(set(word)) == 1:
            prefix += word[0]
        else:
            break
    return prefix


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        words = f.readlines()
        for word in words:
            print(longestCommonPrefix(word.rstrip().split()))