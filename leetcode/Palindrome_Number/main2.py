#!/usr/bin/env python3

def isPalindrome(x:int) -> int:
    if x < 0:
        return False
    if x == 0:
        return True
    reverse_num = 0
    temp = x
    while(temp):
        reverse_num = reverse_num * 10 + temp % 10
        temp = int(temp/10)
    return reverse_num == x
    


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        print(isPalindrome(n))
