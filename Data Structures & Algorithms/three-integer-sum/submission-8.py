class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            num = nums[i]
            rem = 0 - num

            x = i + 1
            y = len(nums) - 1

            while x < y:
                if nums[x] + nums[y] < rem:
                    x += 1
                elif nums[x] + nums[y] > rem:
                    y -= 1
                else:
                    res.append([num, nums[x], nums[y]])
                    x += 1
                    y -= 1
                    while (nums[x] == nums[x-1]) and (x < y):
                        x += 1
        
            while (i < len(nums) - 1) and (nums[i + 1] == num):
                i += 1
            
            i += 1
        
        return res
