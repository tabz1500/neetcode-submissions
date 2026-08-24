class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mp = (l + r) // 2
            if nums[mp] == target:
                return mp
            elif nums[mp] < target:
                if mp < len(nums) - 1:
                    l = mp + 1
                else:
                    break
            else:
                if mp > 0:
                    r = mp - 1
                else:
                    break
        
        return -1