#!/usr/bin/env python3


def lengthOfLongestSubstring(s:str) -> int:
    # find length of longest substring without repeating characters
    length = len(s)
    if len(set(s)) == length:
        #print(f"It's on set {s}, len: {len(s)}")
        return length

    #print(f"check: {s}")
    substring = s[0]
    for i in s[1:]:
        if i in substring:
            break
        substring += i
    #print(f"substring: {substring}, len: {len(substring)}")
    return max(len(substring), lengthOfLongestSubstring(s[1:]))

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        s = f.readline()
        print(lengthOfLongestSubstring(s))