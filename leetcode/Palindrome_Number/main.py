#!/usr/bin/env python3

def isPalindrome(x:int) -> int:
    if x < 0:
        return False
    if x == 0:
        return True
    int_to_string = ""
    while(x):
        int_to_string += str(x % 10)
        x = int(x/10)
    
    return int_to_string == int_to_string[::-1]

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        print(isPalindrome(n))
