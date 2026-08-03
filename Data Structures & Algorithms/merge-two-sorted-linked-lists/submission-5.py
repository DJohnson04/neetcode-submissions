# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        while list1 or list2:
            if list1 == None:
                result.append(list2.val)
                list2 = list2.next
                continue
            if list2 == None:
                result.append(list1.val)
                list1 = list1.next
                continue
            if list1.val < list2.val:
                result.append(list1.val)
                list1 = list1.next
            else:
                result.append(list2.val)
                list2 = list2.next
        head = ListNode(0, None)
        current = head
        for num in result:
            current.next = ListNode(num)
            current = current.next
        return head.next

            