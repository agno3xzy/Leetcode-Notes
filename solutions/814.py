class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return  root if self.checkOne(root) else None

    def checkOne(self, node):
        if node == None:
            return False
        a = self.checkOne(node.left)
        b = self.checkOne(node.right)
        if(not a):
            node.left = None
        if(not b):
            node.right = None
        return node.val == 1 or a or b