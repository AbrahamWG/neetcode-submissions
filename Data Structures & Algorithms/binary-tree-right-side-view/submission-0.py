# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # check left, right
        # len(ret) == level -> first number we see in that level
        ret = [] 
        def dfs(node, level):
            if not node:
                return None
            if level == len(ret):
                ret.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
        dfs(root, 0)
        return ret
