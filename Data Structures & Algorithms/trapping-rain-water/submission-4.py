class Solution:
    def trap(self, height: List[int]) -> int:
        leftmost = []
        rightmost = []

        for i in range(len(height)):
            if i == 0:
                leftmost.append(-1)
                continue
            leftmost.append(max(height[i-1], leftmost[i-1]))
        
        for j in range(len(height) - 1, -1, -1):
            if j == len(height) - 1:
                rightmost.append(-1)
                continue
            rightmost.append(max(height[j + 1], rightmost[-1]))
        
        rightmost.reverse()

        total = 0

        for c in range(len(height)):
            h = height[c]
            if leftmost[c] <= h or rightmost[c] <= h:
                continue
            water = min(leftmost[c], rightmost[c]) - h
            total += water
        
        return total
