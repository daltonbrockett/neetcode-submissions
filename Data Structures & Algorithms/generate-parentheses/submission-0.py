class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        temp = []

        def backtrack(front: int, back: int):
            if n == front == back:
                stack.append("".join(temp))
                return
            
            if front < n:
                temp.append("(")
                backtrack(front + 1, back)
                temp.pop()

            if back < front:
                temp.append(")")
                backtrack(front, back + 1)
                temp.pop()

        backtrack(0, 0)
        return stack
