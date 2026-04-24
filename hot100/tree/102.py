from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        # 双端队列
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            res = []
            for _ in range(len(q)):  # 下面append的操作虽然修改了len,但不会影响到这一行，因为它是先生成好了一个迭代器
                node = q.popleft()
                res.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(res)
        return ans
