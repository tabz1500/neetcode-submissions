class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foo = {}
        for i in nums:
            if foo.get(i):
                return True
            else:
                foo[i] = 1
        return False