from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        while head:
            nxt = head.next
            head.next = temp
            temp = head
            head = nxt
        return temp


if __name__ == '__main__':
    head, last = None, None
    for s in [2,4,3]:
        head = ListNode(int(s))
        head.next = last
        last = head
    head1, last1 = None, None
    for s in [5,6,4]:
        head1 = ListNode(int(s))
        head1.next = last1
        last1 = head1
    print(f'{Solution().reverseList(head) = }')
    print(f'{Solution().reverseList(head1) = }')
