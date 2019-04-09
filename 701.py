# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            if root.val == val:
                return root
            elif root.val > val:
                if root.left:
                    self.insertIntoBST(root.left, val)
                else:
                    newroot = TreeNode(val)
                    root.left = newroot
            else:
                if root.right:
                    self.insertIntoBST(root.right, val)
                else:
                    newroot = TreeNode(val)
                    root.right = newroot
        else:
            root = TreeNode(val)

        return root
