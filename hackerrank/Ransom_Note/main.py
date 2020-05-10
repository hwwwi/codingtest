#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    words = {}
    for word in magazine:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1 
    for word in note:
        if word not in words or words[word] < 1:
            print("No")
            return 
        words[word] -= 1
    
    print("Yes")
    return

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
