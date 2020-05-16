#!/usr/bin/env python3
import sys

def solution(n, m):
    visit = [0] * (n+1)

    def solve(cnt,cur):
        if cnt == m:
            print(' '.join(map(str, cur)))
            
        for i in range(1, n+1):
            if not visit[i]:
                visit[i] = 1
                solve(cnt+1, cur + [i])
                visit[i] = 0     
    solve(0, [])

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    solution(n, m)
