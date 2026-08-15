class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        best = 0
        run = 0
        for r in range(len(s)):
            count[s[r]] += 1
            run += 1
            most = max(count, key=count.get)
            if run - count[most] > k:
                best = max(best, run - 1)
                while (run - count[max(count, key=count.get)]) > k:
                    count[s[l]] -= 1
                    l += 1
                    run -= 1

        return max(best, run)
                