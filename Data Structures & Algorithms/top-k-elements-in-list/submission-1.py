class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        buckets = []
        for i in range(len(nums) + 1): buckets.append([])

        for key in count.keys():
            buckets[count[key]].append(key)
        
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k: return res
        
        return res
            