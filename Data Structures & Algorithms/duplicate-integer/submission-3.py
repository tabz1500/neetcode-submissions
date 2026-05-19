class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foo = set()
        for i in nums:
            if i in foo:
                return True
            else:
                foo.add(i)
        return False