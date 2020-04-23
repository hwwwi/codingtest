#!/usr/bin/env python3
def strStr(haystack:str, needle:str) -> int:
    if not needle:
        return 0
    if (len(haystack) < len(needle)) or (needle not in haystack):
        # checking length is O(1)
        return -1
    return haystack.find(needle)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
      n = f.readlines()
      for i in n:
          haystack, needle = i.rstrip().split()
          print(strStr(haystack, needle))
