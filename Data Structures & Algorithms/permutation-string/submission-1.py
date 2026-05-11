class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counts = Counter(s1)
        for r in range(len(s1) - 1, len(s2)):
            l = r - (len(s1)) + 1
            countsWindow = Counter(s2[l:r + 1])

            if countsWindow == counts:
                return True

        return False