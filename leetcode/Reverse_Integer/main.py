#!/usr/bin/env python3

def reverse(x:int) -> int:
    if x == 0:
        return 0
    sign = -1 if x < 0 else 1
    int_to_str = ""
    x = abs(x)
    while(x):
        int_to_str += str(x%10)
        x = int(x/10)
    
    result = sign * int(int_to_str)
    if((2 ** 31 - 1) <= result or result <= -1 * (2 ** 31)):
        return 0    
    
    return sign * int(int_to_str)
    

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        print(reverse(n))
