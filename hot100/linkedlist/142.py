from typing import Optional


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 两种方法：1.哈希表set；2.双指针(Floyd判圈算法)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:  # 二者相遇时，fast多走的距离=圈的长度=slow走的距离
                while head is not slow:  # 因此 slow这圈还没走完的距离=已经走的总距离-圈上走过的距离=从head走到相遇点的距离，因此此时head和slow同时相同速度出发就能在圈的入口相遇
                    head = head.next
                    slow = slow.next
                return slow
        return None
