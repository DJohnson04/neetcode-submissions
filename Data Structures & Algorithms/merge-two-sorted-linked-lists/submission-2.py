# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        left_p = list1
        right_p = list2
        result = []
        while left_p != None or right_p != None:
            if left_p == None:
                result.append(right_p.val)
                right_p = right_p.next
                continue
            if right_p == None:
                result.append(left_p.val)
                left_p = left_p.next
                continue
            if left_p.val <= right_p.val:
                result.append(left_p.val)
                left_p = left_p.next
            else:
                result.append(right_p.val)
                right_p = right_p.next
        head = ListNode(result[0], None)
        curr = head
        for num in range(1, len(result)):
            curr.next = ListNode(result[num], None)
            curr = curr.next
        return head
