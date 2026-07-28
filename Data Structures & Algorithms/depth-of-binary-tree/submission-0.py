# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        queue = [root]

        layers = []

        while queue:
            
            layer = []

            for element in range(len(queue)):
                node = queue.pop(0)
                if node != None:
                    layer.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if len(layer) > 0:
                layers.append(layer)
        
        return len(layers)


        