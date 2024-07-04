# Definition for singly-linked list.

# class ListNode:

#     def __init__(self, val=0, next=None):

#         self.val = val

#         self.next = next

class Solution:

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head.next  # 첫 번째 0 다음 노드부터 시작

        new_head = ListNode(0)  # 새로운 리스트의 더미 헤드

        new_current = new_head

        sum_val = 0



        while current:

            if current.val == 0:

                new_current.next = ListNode(sum_val)

                new_current = new_current.next

                sum_val = 0

            else:

                sum_val += current.val

            current = current.next



        return new_head.next
