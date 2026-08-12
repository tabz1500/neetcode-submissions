class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = 0
        y = len(s) - 1
        while x < y:
            print(f"X pos: {s[x]}")
            if not s[x].isalnum():
                x += 1
                continue
            while not s[y].isalnum():
                y -= 1

            if s[y] != s[x]:
                return False
            else:
                x += 1
                y -= 1
        return True