class Solution:
    def findMin(self, nums: List[int]) -> int:  
        l, r = 0, len(nums) - 1

        while l < r:
            mp = (l + r) // 2

            if nums[mp] > nums[r]:
                l = mp + 1
            else:
                r = mp
        
        return nums[l]
