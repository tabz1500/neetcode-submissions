class Solution:
    def findMin(self, nums: List[int]) -> int:  
        if nums[0] < nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1

        while l < r:
            mp = (l + r) // 2

            if nums[mp] > nums[r]:
                l = mp + 1
            else:
                r = mp
        
        return nums[l]
