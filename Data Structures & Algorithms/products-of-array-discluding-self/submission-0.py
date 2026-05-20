class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        out = []

        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1]*nums[i - 1])
        
        for i in range(1, len(nums)):
            suffix.append(suffix[i - 1]*nums[len(nums) - i])
        suffix.reverse()

        print(prefix)
        print(suffix)

        for i in range(len(nums)):
            out.append(prefix[i]*suffix[i])
        
        return out
