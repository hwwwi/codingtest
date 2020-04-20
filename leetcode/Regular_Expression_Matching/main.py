#!/usr/bin/env python3

def isMatch(text:str, pattern:str) -> bool:
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        # zero or more
        return (isMatch(text, pattern[2:]) or
                first_match and isMatch(text[1:], pattern))
    else:
        # same chracter
        return first_match and isMatch(text[1:], pattern[1:])

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        s = f.readline().rstrip()
        p = f.readline().rstrip()
        print(isMatch(s,p))