class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = {}
        out = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for num in counts:
            buckets[counts.get(num)].append(num)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                out.append(num)
                k -= 1
                if k == 0:
                    return out
        return out