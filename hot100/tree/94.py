from typing import Optional

class TreeNode:
    def __init__(self, val: int=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 两种写法，递归和线索二叉树(Morris遍历，迭代)
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        ans = []
        dfs(root)
        return ans

    def morrisTraversal(self, root: Optional[TreeNode]) -> list[int]:
        ans = []
        while root:
            if root.left:
                # 找 root 的前驱 pre：在中序遍历中，root 的上一个节点
                # 从 root.left 开始，一直向右走，直到走到尽头，或者遇到指向 root 的线索（回到 root 的路）。
                pre = root.left
                while pre.right and pre.right is not root:
                    pre = pre.right
                # root 的左子树尚未访问
                if pre.right is None:
                    pre.right = root
                    root = root.left
                    continue
                # root 的左子树访问完毕，去掉线索，恢复原样
                pre.right = None  # 注：如果调用完 inorderTraversal 不再使用这棵二叉树，这行代码可以去掉
            # root 的左子树访问完毕
            ans.append(root.val)  # 记录当前节点的值
            root = root.right  # 如果有右子树就访问右子树，没有就顺着线索回到指向的节点
        return ans
