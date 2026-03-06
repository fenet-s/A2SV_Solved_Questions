# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        count = 0
        current = head
        while current:
            count += 1
            current = current.next 
        
        to_be_removed = count - (n)
        
        temp = dummy
        for _ in range(to_be_removed):
            temp = temp.next
        temp.next = temp.next.next 

        return dummy.next


        