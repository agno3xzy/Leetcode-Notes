# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            ans.append(root.node)
            inorder(root.right)
        return inorder(root)