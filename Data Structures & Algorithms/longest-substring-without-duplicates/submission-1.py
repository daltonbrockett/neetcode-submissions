class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        seen = set()
        seen.add(s[0])
        maxSeen = 1
        l, r = 0, 1
        while r < len(s):
            charL, charR = s[l], s[r]
            while charR in seen:
                seen.remove(charL)
                l += 1
                charL = s[l]
            seen.add(charR)
            maxSeen = max(maxSeen, r - l + 1)
            r += 1
        return maxSeen