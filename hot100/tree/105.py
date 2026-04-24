from typing import Optional


class TreeNode:
    def __init__(self, val: int=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # 两种方法：1.递归；2.使用hash表优化方法1
        if not preorder:  # 前序遍历序列为空（遍历到叶子节点）
            return None
        left_size = inorder.index(preorder[0])  # 找根节点在中序中的位置，确定左子树的大小
        left = self.buildTree(preorder[1:left_size + 1], inorder[:left_size])  # 递归构造左右子树，返回左右子树的根节点，也就是当前节点的左右儿子
        right = self.buildTree(preorder[left_size + 1:], inorder[left_size + 1:])
        return TreeNode(preorder[0], left, right)
