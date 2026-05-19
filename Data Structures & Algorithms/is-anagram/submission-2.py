class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        foo = {}
        for i in range(len(s)):
            foo[s[i]] = 1 + foo.get(s[i], 0)
            foo[t[i]] = foo.get(t[i],0) - 1
        
        for j in foo.values():
            if j != 0:
                return False
        
        return True