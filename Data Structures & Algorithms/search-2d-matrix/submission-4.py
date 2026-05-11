class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Single numbers iteration, (r,c) represented by 
            # r = num // len(matrix)
            # c = num % len(matrix[0])
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            num = matrix[m//len(matrix[0])][m%len(matrix[0])]
            if num < target:
                l = m + 1
            elif num > target:
                r = m - 1
            else:
                return True
        return False
