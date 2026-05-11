class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.validChar(s[l]):
                l += 1

            while l < r and not self.validChar(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def validChar(self, char):
        unicode = ord(char)
        return (ord('a') <= unicode and unicode <= ord('z') or
               ord('A') <= unicode and unicode <= ord('Z') or
               ord('0') <= unicode and unicode <= ord('9'))