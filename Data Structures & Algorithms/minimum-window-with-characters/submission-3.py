class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        count = {}
        for i in t:
            count[i] = count.get(i, 0) + 1

        window = {}
        target = len(count)
        l = 0
        r = 0

        bestl = -1
        bestr = -1

        bestCount = float('inf')
        have = 0
        
        while r < len(s):
            if s[r] in count:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == count[s[r]]: have += 1

            while have == target:
                if  (r - l + 1) < bestCount:
                    bestCount = len(s[l:r+1])
                    bestl = l
                    bestr = r 
                
                if s[l] in count:
                    window[s[l]] = window.get(s[l], 0) - 1
                    if window[s[l]] < count[s[l]]:
                        have -= 1
                
                l += 1
            
            r += 1
        
        return s[bestl:bestr + 1]


