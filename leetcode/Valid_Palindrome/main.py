#!/usr/bin/env python3

class Solution:
    def resolve(self, s: str) -> bool:
        sp = 0 # start point
        ep = len(s) - 1 # end point
        s = s.lower()
        
        while(sp <= ep):
            sv = s[sp] # start value
            ev = s[ep] # end value
            print(f"sv:{sv}, ev:{ev}")
            if not ('A' <= sv <= 'Z' or 'a' <= sv <= 'z' or '0' <= sv <= '9'):
                sp += 1
            elif not ('A' <= ev <= 'Z' or 'a' <= ev <= 'z'or '0' <= ev <= '9'):
                ep -= 1
            else:
                if sv != ev:
                    return False
                sp += 1
                ep -= 1
        return True


