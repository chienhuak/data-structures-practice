# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# head = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))

# 雙指針反轉鏈結串列
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        pre = None
        while curr : 
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre