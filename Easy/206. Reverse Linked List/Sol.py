# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        dummy = None
        curr = head

        while curr:
            cachedNext = curr.next

            # Reverse the link
            curr.next = dummy

            # Advance pointers
            dummy = curr
            curr = cachedNext
        
        return dummy