#!/usr/bin/env python3

def isValid(s: str) -> bool:
    stack = []
    match = {'(':')', '{':'}', '[':']'}

    for bracket in s:
        # print(f"braket: {bracket}")
        if bracket in match:
            stack.append(bracket)
        else:
            if not stack:
                return False
            opens = stack.pop()
            # print(f"opens: {opens}")
            if bracket != match[opens]:
                return False
    return not stack

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        s = f.readlines()
        for parentheses in s:
            print(isValid(parentheses.rstrip()))
            print("--------------------")