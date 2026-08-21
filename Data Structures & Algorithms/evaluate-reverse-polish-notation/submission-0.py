class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for i in tokens:
            if i in operators:
                y = stack.pop()
                x = stack.pop()

                if i == '+': stack.append(x + y)
                elif i == '-': stack.append(x - y)
                elif i == '*': stack.append(x * y)
                elif i == '/': stack.append(int(x / y))
            else:
                stack.append(int(i))
        
        return stack.pop()
