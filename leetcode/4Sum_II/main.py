#!/usr/bin/env python3

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans=0
        di={}
        
        for i in A:
            for j in B:
                if i+j not in di:
                    di[i+j]=1
                else:
                    di[i+j]+=1
        
        for i in C:
            for j in D:
                if -i-j in di:
                    ans+=di[-i-j]
        
        return ans