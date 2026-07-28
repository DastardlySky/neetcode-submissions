# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def treeList(root):
            queue = [root]
            treeList = []

            while queue:

                layer = []

                for element in range(len(queue)):
                    node = queue.pop(0)

                    if node:
                        layer.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        layer.append(None)

                if len(layer) > 0:
                    treeList.append(layer)

            return treeList

        print(treeList(p), treeList(q))
        return treeList(p) == treeList(q)