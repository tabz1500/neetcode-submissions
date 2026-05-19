class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        foo = {}
        for i in range(len(s)):
            if s[i] in foo:
                foo[s[i]] += 1
            else:
                foo[s[i]] = 1
            
            if t[i] in foo:
                foo[t[i]] -= 1
            else:
                foo[t[i]] = -1
        
        for j in foo.values():
            if j != 0:
                return False
        
        return True