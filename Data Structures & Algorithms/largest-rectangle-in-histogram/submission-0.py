class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            curr = heights[i]
            if stack and curr < stack[-1][1]:
                while stack and stack[-1][1] > curr:
                    discard = stack.pop()
                    maxArea = max(maxArea, discard[1] * (i - discard[0]))
                stack.append([discard[0], curr])
            else:
                stack.append([i, curr])
        
        while stack:
            curr = stack.pop()
            maxArea = max(maxArea, curr[1] * (len(heights)  - curr[0]))
        
        return maxArea