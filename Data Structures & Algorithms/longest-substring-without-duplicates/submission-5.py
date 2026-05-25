class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        maxL = 1
        dups = {s[0]: 0}
        start = 0

        for i in range(1, len(s)):
            if s[i] in dups:
                start = max(start, dups[s[i]] + 1)
            maxL = max(maxL, i - start + 1)
            dups[s[i]] = i


        return maxL     