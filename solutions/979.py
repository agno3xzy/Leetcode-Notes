# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            L, R = dfs(root.left), dfs(root.right)
            self.ans += abs(L) + abs(R)
            return root.val + L + R - 1
        dfs(root)
        return self.ans