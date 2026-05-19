class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foo = {}
        for i in nums:
            if i in foo:
                return True
            else:
                foo[i] = 1
        return False