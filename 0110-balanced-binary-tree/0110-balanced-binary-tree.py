# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)

        return height(root) != -1
        
        
        # balanced = [True]

        # def balance(root):
        #     if not root:
        #         return 0
            
        #     left_side = balance(root.left)
        #     if balanced[0] is False:
        #         return 0
        #     right_side = balance(root.right)

        #     if abs(left_side - right_side) > 1:
        #         balanced[0] = False
        #         return 0
        #     return 1 + max(left_side, right_side)
        # balance(root)
        # return balanced[0]