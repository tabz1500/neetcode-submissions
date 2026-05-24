class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for num in nums:
            if num - 1 in numset: continue
            i = num + 1
            count = 1
            while i in numset:
                count += 1
                i += 1
            res = max(count, res)
        
        return res