# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        lag = head
        if head.next == None:
            return head

        temp = head.next
        head.next = None
        while temp.next != None:
            lag = temp
            temp = temp.next
            lag.next = head
            head = lag
        temp.next = head
        head = temp
        return head

        
            
        