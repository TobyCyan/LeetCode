from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        seen = set()
        ptr = head
        while ptr:
            if ptr in seen:
                return ptr
            
            seen.add(ptr)
            ptr = ptr.next
        
        return None