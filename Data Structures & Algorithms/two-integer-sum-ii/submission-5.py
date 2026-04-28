class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        if length < 2:
            return None
        listy = []
        front = 0
        curr = 1
        while numbers[front] + numbers[curr] != target:
            if not(length - 1 == curr):
                curr += 1
            else:
                front += 1
                if front == length - 1:
                    return None
                curr = front + 1
        listy.append(front + 1)
        listy.append(curr + 1)
        return listy
        
            
