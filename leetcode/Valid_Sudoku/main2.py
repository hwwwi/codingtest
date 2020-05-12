#!/usr/bin/env python3

from collections import Counter

from typing import List
class Solution:
    def resolve(self, board: List[List[str]]) -> bool:
        # vertical
        for i in range(9):
            check = [0] * 10
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if check[int(board[i][j])]:
                    return False
                check[int(board[i][j])] = 1
        
        # parallel
        for i in range(9):
            check = [0] * 10
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if check[int(board[j][i])]:
                    return False
                check[int(board[j][i])] = 1

        # square
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                check = [0] * 10
                for k in range(i, i+3):
                    for h in range(j, j+3):
                        # print(f"k:{k}, h:{h},var:{board[k][h]} check: {check}")
                        if board[k][h] == '.':
                            continue
                        if check[int(board[k][h])]:
                            return False
                        check[int(board[k][h])] = 1

        return True