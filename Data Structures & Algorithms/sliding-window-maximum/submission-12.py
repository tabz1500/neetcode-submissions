
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return [max(nums)]
        
        q = deque()
        res = []

        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        
        res.append(nums[q[0]])
        
        for r in range(k, len(nums)):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            if q and q[0] <= r - k:
                q.popleft()
            q.append(r)
            res.append(nums[q[0]])
        
        return res