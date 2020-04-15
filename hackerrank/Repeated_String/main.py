#!/usr/bin/env python3

def repeatedString(s, n):
    count_a = list(s).count('a')
    length = len(s)
    repeat = n // length
    left = n % length
    left_a = list(s[:left]).count('a')
    return count_a * repeat + left_a

if __name__ == '__main__':
    # The first line contains a single string, s
    # The second line contains an integer, n

    with open('input.txt', 'r') as f:
        s = f.readline().replace('\n','')
        n = int(f.readline())
    
    result = repeatedString(s, n)
    print(result)