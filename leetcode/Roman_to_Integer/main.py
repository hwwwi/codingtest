#!/usr/bin/env python3

def romanToInt(s:str) -> int:
    result = 0

    symbols = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C':100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M':1000
    }
    while(s):
        #print(f"{s}, {result}")
        if len(s) >= 2 and s[:2] in symbols:
            result += symbols[s[:2]]
            s = s[2:]
        else:     
            result += symbols[s[0]]
            s = s[1:]
    return result

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        numbers = f.readlines()
        for number in numbers:
            print(romanToInt(number.rstrip()))