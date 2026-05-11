class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        for num in counts:
            buckets[counts[num]].append(num)

        out = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                k -= 1
                out.append(num)
                if k == 0:
                    return out