# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(node, greatest):
            nonlocal good
            if not node:
                return 
            if node.val >= greatest:
                good += 1
                greatest = max(greatest, node.val)
            dfs(node.left, greatest)
            dfs(node.right, greatest)
        dfs(root, root.val)
        return good