# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        def mirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return (mirror(left.left, right.right) and mirror(left.right, right.left))
        
        return mirror(root.left, root.right)



        # def symm(root1, root2):
        #     if not root1 and not root2:
        #         return True
        #     if not root1 or not root2:
        #         return False
            
        #     if root1.val != root2.val:
        #         return False
        #     return symm(root1.left, root2.right) and \
        #            symm(root1.right, root2.left)

        # return symm(root, root)

