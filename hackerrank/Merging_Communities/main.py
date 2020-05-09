#!/usr/bin/env python3

import sys

class Solution:
    def union_find(self, n: int, q: int):
        community = list(range(n+1))
        count = [1] * (n+1)

        def find(n: int):
            if n == community[n]:
                return n
            community[n] = find(community[n])
            return community[n]

        def union(a: int, b: int):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return
            community[root_b] = root_a
            count[root_a] = count[root_a] + count[root_b]

        for _ in range(q):
            query = sys.stdin.readline().strip().split()
            if query[0] == 'Q':
                person = int(query[1])
                print(count[find(person)])
            elif query[0] == 'M':
                a, b = [int(x) for x in query[1:]]
                union(a,b)
                # print(f"a: {a}, b:{b}, community: {community}, count: {count}")

if __name__ == "__main__":
    """
    n: numbers of people
    q: numbers of query
    """

    sys.setrecursionlimit(100000)
    n,q = [int(x) for x in input().split()]
    Solution().union_find(n, q)