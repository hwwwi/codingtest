#!/usr/bin/env python3

def fibonacci(n):
    # Write your code here.
    fib = [0] * (n+1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


n = int(input())
print(fibonacci(n))