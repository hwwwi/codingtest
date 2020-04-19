#!/usr/bin/env python3


def lengthOfLongestSubstring(s:str) -> int:
    # find length of longest substring without repeating characters
    substring = []
    max_num = 0
    for val in s:
        if val in substring:
            substring = substring[substring.index(val) + 1:]
        substring.append(val)
        max_num = max(max_num, len(substring))
    return max_num
        
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        s = f.readline()
        print(lengthOfLongestSubstring(s))