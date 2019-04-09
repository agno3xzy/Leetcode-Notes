# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        return self.consturct(preorder, 0, len(preorder)-1)
    def consturct(self, preorder, start, end):
        if(start > end):
            return  None
        root = TreeNode(preorder[start])
        index = start
        while index <= end:
            if preorder[index] > root.val:
                break
            index = index + 1

        root.left = self.consturct(preorder, start + 1, index-1)
        root.right = self.consturct(preorder,index, end)
        return root


p = [8,5,1,7,10,12]
s = Solution()
print(s.bstFromPreorder(p))
