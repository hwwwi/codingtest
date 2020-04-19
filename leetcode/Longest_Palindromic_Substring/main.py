#!/usr/bin/env python3

def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s
        
    start,offset=0,0 # start and offset of palindrome
    for check in range(len(s)):
        #print(f"start:{start}, check:{check}, offset:{offset}, s: {s[check-offset: check+1]}, s2: {s[check-offset-1: check+1]}")
        if s[check-offset: check+1] == s[check-offset: check+1][::-1]:
            start, offset = check-offset, offset+1
        elif check-offset > 0 and s[check-offset-1: check+1] == s[check-offset-1: check+1][::-1]:
            start, offset = check-offset-1, offset+2
    return s[start: start+offset]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        s = f.readline()
        print(longestPalindrome(s))
