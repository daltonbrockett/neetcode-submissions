class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        for char in s:
            if (char == '{' or
                char == '[' or
                char == '('):
                stack.append(char)
            else:
                if not stack:
                    return False
                other = stack.pop()
                if ((char == '}' and other !='{') or
                    (char == ']' and other != '[') or
                    (char == ')' and other != '(')):
                    return False
        return True if not stack else False