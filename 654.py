# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxIndex(self, nums, l, r):
        if r == len(nums) and l==0:
            return nums.index(max(nums))
        else:
            numspar = nums[l:r]
            return nums.index(max(numspar))

    def way(self, nums, l, r):
        if nums == []:
            return None
        maxindex = self.maxIndex(nums, l, r)
        root = TreeNode(nums[maxindex])
        root.left = self.way(nums, l, maxindex)
        root.right = self.way(nums, maxindex+1, r)
        return root
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

