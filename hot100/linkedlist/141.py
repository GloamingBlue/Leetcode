from typing import Optional


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head  # 快慢指针，时间复杂度O(n)，空间O(1)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:  # 使用内存地址是否一致进行比较，所以是is
                return True
        return False
