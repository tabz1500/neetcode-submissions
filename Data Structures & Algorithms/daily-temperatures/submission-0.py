class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # if the number is larger than the next one, but the next one has a larger number than it after it, preemtively add the pop counts to the larger number before, if it remains in the stack, set the count fo rit to 0, i.e. any of the indexes left in the stack at the end should have counts of 0, actually no need, just do index math.

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                start = stack.pop()
                res[start] = i - start
            stack.append(i)
        
        return res
