class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        loc = defaultdict(lambda: -1)
        l = 0
        r = 0
        best = 0
        res = 0

        while l < len(s) and r < len(s):
            if loc[s[r]] == -1 or loc[s[r]] < l:
                loc[s[r]] = r
                res += 1
                r += 1
            else:
                l = loc[s[r]] + 1
                loc[s[r]] = r
                best = max(res, best)
                res = r - l + 1
                r += 1
        return max(best, res)