# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #cannot access specific index, msut find length of the list, then find length - n = how many steps we need to go. save head, replace and then continue

        length = 0
        current = head
        while current != None:
            current = current.next
            length += 1
        if length == 0:
            return None
        if n == length:
            return head.next
        # Loop through linked list until we find nth-1 node, then change the .next to .next.next or none if n = 1
        i = 0
        curr = head
        while i != length - n - 1 and i < length:
            curr = curr.next
            i += 1
        if n == 1:
            curr.next = None
        else:
            curr.next = curr.next.next
        return head
        

        