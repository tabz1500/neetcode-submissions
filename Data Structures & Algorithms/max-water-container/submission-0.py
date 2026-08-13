class Solution:
    def maxArea(self, heights: List[int]) -> int:
        top = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            top = max(water, top)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return top
