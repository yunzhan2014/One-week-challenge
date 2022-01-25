from typing import List


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    


class LinkList:

    def __init__(self) -> None:
        self.head = None


    def add(self, *node):
        if not node:
            print("Please input node val")
        while node:
            return None

    
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        dmp = cur = ListNode(0)
        cur.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dmp.next     

    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        delete duplicate node in order linked list
        """
        cur = ListNode(0)
        cur.next = head
        if not head: return None
        while head.next:
            if head.val == head.next.val:
                head.next  = head.next.next
            else:
                head = head.next
        return cur.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        19 leetcode
        remove nth node from end                                
        """
        if not head: return None
        dump = ListNode(0)
        dump.next = head
        node_num = 0
        while head:
            node_num += 1
            head = head.next
        times = node_num - n
        j = 0
        if times ==0:
            dump.next == dump.next.next
        else:
            while head:
                j += 1
                if j == times:
                    head.next = head.next.next
                    break
                else:
                    head = head.next
        return dump.next