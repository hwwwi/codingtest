#!/usr/bin/env python3
def strStr(haystack:str, needle:str) -> int:
    if not needle:
        return 0
    haystack_len = len(haystack)
    needle_len = len(needle)
    if (haystack_len < needle_len) or not haystack:
        # checking length is O(1)
        return -1
    for i in range(haystack_len):
        if haystack[i:i+needle_len] == needle:
            return i
    return -1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
      n = f.readlines()
      for i in n:
          haystack, needle = i.rstrip().split()
          print(strStr(haystack, needle))
