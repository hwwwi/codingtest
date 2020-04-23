#!/usr/bin/env python3

def calc(num:str) -> str:
    result = ""
    check = ""
    count = 0
    idx = 0
    length = len(num)
    while(True):
        #print(f"idx: {idx}, check: {check}, count: {count}")
        if idx == length:
            result += (str(count) + check)
            return result
        if not check:
            check = num[idx]
            idx += 1
            count = 1
        elif check == num[idx]:
            count += 1
            idx += 1
        else:
            result += (str(count) + check)
            check = ""

def resolve(n: int) -> str:
    result = "1"
    for _ in range(1, n):
        result = calc(result)
    return result

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        nums = f.readlines()
        for n in nums:
            print(resolve(int(n.rstrip())))
            print("----------------")
          
