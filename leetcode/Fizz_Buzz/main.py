#!/usr/bin/env python3
from typing import List 
def fizzbuz(n: int) -> List[str]:
    result = []
    for i in range(1, n+1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        num = int(f.readline().rstrip())
        print(fizzbuz(num))