from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ls1, ls2, i, j, res = [], [], 0, 0, ''
        while l1:
            ls1.append(l1.val)
            l1 = l1.next
            i += 1
        while l2:
            ls2.append(l2.val)
            l2 = l2.next
            j += 1
        if i < j:
            for k in range(0, i):
                res = str((ls1[k] + ls2[k]) % 10) + res
                ls2[k+1] += (ls1[k] + ls2[k]) // 10
            for k in range(i, j - 1):
                res = str(ls2[k] % 10) + res
                ls2[k+1] += ls2[k] // 10
            res = str(ls2[j-1]) + res
        elif i > j:
            for k in range(0, j):
                res = str((ls1[k] + ls2[k]) % 10) + res
                ls1[k+1] += (ls1[k] + ls2[k]) // 10
            for k in range(j, i - 1):
                res = str(ls1[k] % 10) + res
                ls1[k+1] += ls1[k] // 10
            res = str(ls1[i-1]) + res
        else:
            for k in range(0, i-1):
                res = str((ls1[k] + ls2[k]) % 10) + res
                ls1[k+1] += (ls1[k] + ls2[k]) // 10
            res = str(ls1[i-1] + ls2[i-1]) + res
        head, last = None, None
        for s in res:
            head = ListNode(int(s))
            head.next = last
            last = head
        return head


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
    print(Solution.addTwoNumbers(head, head1).val)  # [7,0,8]
    # print(Solution.addTwoNumbers([0], [0]))  # [0]
    # print(Solution.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))  # [8,9,9,9,0,0,0,1]
