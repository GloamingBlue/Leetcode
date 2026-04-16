from typing import Optional


class ListNode:
    def __init__(self, val: int=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 尾插法(新建链表，使用哨兵节点记录链表头)；头插法(递归实现)
        if list1 is None: return list2
        if list2 is None: return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
