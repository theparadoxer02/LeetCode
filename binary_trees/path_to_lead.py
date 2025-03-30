from typing import Optional, List


class Solution:
    def binaryTreePaths(self, root) -> List[str]:
        final = []
        
        def inorder(node, path):
            if not node:
                return path
            
            if not node.left and not node.right:
                final.append(path)

            if node.left:
                temp_path = f"{path}->{str(node.left.val)}"
                inorder(node.left, path=temp_path)

            if node.right:
                temp_path = f"{path}->{str(node.right.val)}"
                inorder(node.right, path=temp_path)

        inorder(root, path="")
        return final


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Helper function to create a binary tree for testing
def create_tree(values):
    """
    Create a binary tree from a list of values. 
    None values indicate the absence of a node.
    Example:
        values = [1, 2, 3, None, 5]
        Tree:
            1
           / \
          2   3
           \
            5
    """
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    
    return root

# Example usage:
values = [1, 2, 3, None, 5]
root = create_tree(values)
solution = Solution()
paths = solution.binaryTreePaths(root)
print(paths) 