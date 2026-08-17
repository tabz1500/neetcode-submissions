class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        need = [0] * 128
        for i in t:
            need[ord(i)] += 1
        
        missing = len(t)
        l = 0
        r = 0

        bestl = 0
        bestr = -1

        bestCount = float('inf')
        have = 0
        
        while r < len(s):
            if need[ord(s[r])] > 0:
                missing -= 1
            
            need[ord(s[r])] -= 1

            if missing == 0:
                
                while l < r and need[ord(s[l])] < 0:
                    need[ord(s[l])] += 1
                    l += 1
                
                if  (r - l + 1) < bestCount:
                    bestCount = (r - l + 1)
                    bestl = l
                    bestr = r
                
                need[ord(s[l])] += 1
                missing += 1
                l += 1
            
            r += 1
        
        return s[bestl:bestr + 1]


