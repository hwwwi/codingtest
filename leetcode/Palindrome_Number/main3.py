#!/usr/bin/env python3

def isPalindrome(x:int) -> int:
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        print(isPalindrome(n))
