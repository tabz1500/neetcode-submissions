class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mp = (l + r) // 2

            if nums[mp - 1] > nums[mp]:
                return nums[mp]
            elif nums[( mp + 1) % len(nums)] < nums[mp]:
                return nums[( mp + 1) % len(nums)]
            else:
                if nums[mp] < nums[r]:
                    r = mp
                else:
                    l = mp + 1
