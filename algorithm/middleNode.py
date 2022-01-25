class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast:
            if not fast.next:
                return slow
            if not fast.next.next:
                return slow.next
            fast = fast.next.next
            slow = slow.next
        return slow

if __name__ == "__mian__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    head = node1

    s = Solution()
    midNode = s.middleNode(head)
    while midNode:
        print(midNode.val)
        midNode = midNode.next