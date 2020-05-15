#!/usr/bin/env python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the freqQuery function below.
def freqQuery(queries):
    d = defaultdict(lambda: 0)
    f = defaultdict(lambda: 0)
    output = []
    for command, key in queries: # O(n) queries
        if command == 1:
            f[d[key]] = max(0, f[d[key]] - 1)
            d[key] += 1
            f[d[key]] += 1
        elif command == 2:
            f[d[key]] = max(0, f[d[key]] - 1)
            d[key]= max(0, d[key] - 1)
            if d[key] > 0:
                f[d[key]] += 1
        else:
            if f[key] > 0: # O(1)
                output.append(1)
            else:
                output.append(0)
    return output
            

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
