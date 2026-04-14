from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:  # 快慢指针，找的是中间节点(奇数个)或右半第一个节点(偶数个)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # 链表反转
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)  # 原来链表的最后一个节点
        while head2:  # 结束条件是head2为None，也就是到达了最中间节点的子节点，此时代表着左右两半的链表判断完毕
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
