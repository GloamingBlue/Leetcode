from typing import Optional
from heapq import heapify, heappop, heappush


class ListNode:
    def __init__(self, val: int=0, next=None) -> None:
        self.val = val
        self.next = next


ListNode.__lt__ = lambda a, b : a.val < b.val  # 构造魔法方法，配合heapq


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # 最小堆：堆中放入最小的候选节点，每次最小元素出堆就可以放入这个元素的子节点作为候选节点
        cur = dummy = ListNode()
        h = [head for head in lists if head]  # 初始化时放入所有的非空头节点，因为最小的一定在它们之中
        heapify(h)  # 堆化
        while h:
            node = heappop(h)
            if node.next:
                heappush(h, node.next)
            cur.next = node
            cur = cur.next
        return dummy.next