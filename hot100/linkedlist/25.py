from typing import Optional


class ListNode:
    def __init__(self, val: int=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        p0 = dummy = ListNode(next=head)  # 设置哨兵节点，p0为每一段的起始节点的父节点
        pre = None
        cur = head

        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next  # nxt辅助p0更新位置
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next
