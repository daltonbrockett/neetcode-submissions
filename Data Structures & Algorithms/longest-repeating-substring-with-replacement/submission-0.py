class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowCounts = defaultdict(int)
        l = 0
        maxFreq = 0
        overallMax = 0
        for r in range(len(s)):
            windowCounts[s[r]] += 1
            maxFreq = max(maxFreq, windowCounts[s[r]])
            while (r - l) - maxFreq + 1 > k:
                windowCounts[s[l]] -= 1
                l += 1
            overallMax = max(overallMax, r - l + 1)
        return overallMax