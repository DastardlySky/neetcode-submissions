# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = [root]

        layers = []

        res = []

        while queue:

            layer = []

            for element in range(len(queue)):

                node = queue.pop(0)

                if node:

                    layer.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            if len(layer) > 0:
                layers.append(layer)
        

        for layer in layers:
            res.append(layer[-1])

        return res