# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def maxTree(self,nums):
        maxIndex = nums.index(max(nums))
        node = TreeNode(nums[maxIndex])
        if len(nums[maxIndex+1:]>0):
            node.right = self.maxTree(nums[maxIndex+1:])
        if len(nums[:maxIndex]>0):
            node.left = self.maxTree(nums[:maxIndex])
        return node
    def constructMaximumBinaryTree(self, nums):
        return self.maxTree(nums)

