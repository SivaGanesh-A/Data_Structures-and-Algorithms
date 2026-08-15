# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #split two halfs
        second = slow.next
        slow.next = None
        #reverse second half
        previous = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = previous
            previous = curr
            curr = next_node
        second = previous
        #merge alternatively
        first = head
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next