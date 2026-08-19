class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')': '(', '}': '{', ']': '['}

        stack = []

        for i in s:
            if i in bracket.values():
                stack.append(i)
            if i in bracket:
                if len(stack) == 0: return False
                if stack[-1] != bracket[i]:
                    return False
                stack.pop()
        
        if stack:
            return False
        
        return True