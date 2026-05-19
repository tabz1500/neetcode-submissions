class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            minitarget = target - nums[i]
            if minitarget in seen:
                return [seen[minitarget], i]
            else:
                seen[nums[i]] = i