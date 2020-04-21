#!/usr/bin/env python3

from typing import List
def longestCommonPrefix(strs:List[str]) -> str:
    if len(strs)==0:
        return ""
    if len(strs)==1:
        return strs[0]
    length = min([len(s) for s in strs]) 
    result = ""
    for i in range(length):
        ch = [s[i] for s in strs]
        if len(set(ch)) == 1:
            result += ch[0]
        else:
            break
    return result


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        words = f.readlines()
        for word in words:
            print(longestCommonPrefix(word.rstrip().split()))