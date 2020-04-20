#!/usr/bin/env python3

def isMatch(text:str, pattern:str) -> bool:
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        s = f.readline().rstrip()
        p = f.readline().rstrip()
        print(isMatch(s,p))