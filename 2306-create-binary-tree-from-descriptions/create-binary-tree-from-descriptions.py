# Definition for a binary tree node.
#class TreeNode(object):
#   def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
class Solution(object):
    def createBinaryTree(self, nodes):
        children = set()
        node_map = {}

        for node in nodes:
            parent = node[0]
            child = node[1]
            isLeft = node[2]

            children.add(child)

            if parent not in node_map:
                node_map[parent] = TreeNode(parent)

            if child not in node_map:
                node_map[child] = TreeNode(child)

            parent_node = node_map[parent]
            child_node = node_map[child]

            if isLeft == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

        for node in nodes:
            parent = node[0]
            if parent not in children:
                return node_map[parent]
        return None       