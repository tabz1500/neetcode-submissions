class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0: break
            if (i > 0) and (nums[i-1] == n):
                continue

            lo = i + 1
            hi = len(nums) - 1

            target = 0 - n

            while lo < hi:
                if (nums[lo] + nums[hi]) < target:
                    lo += 1
                elif (nums[lo] + nums[hi]) > target:
                    hi -= 1
                else:
                    res.append([n, nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while (nums[lo] == nums[lo - 1]) and (lo < hi):
                        lo += 1
            
        return res