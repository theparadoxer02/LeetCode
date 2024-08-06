class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def build_tree(self, values):
        if not values:
            return None

        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i in range(len(nodes)):
            if nodes[i] is not None:
                left_child_index = 2 * i + 1
                right_child_index = 2 * i + 2

                if left_child_index < len(nodes):
                    nodes[i].left = nodes[left_child_index]

                if right_child_index < len(nodes):
                    nodes[i].right = nodes[right_child_index]

        return nodes[0]  # Return the root of the binary tree

# Example usage:
# Let's create a binary tree with values [1, 2, 3, 4, None, 5, 6].

binary_tree = BinaryTree()
# tree_values = [1, 2, 3, None, 5, None, 4]
# tree_values = [3, 9, 20, None, None, 15, 7]
tree_values = [2,1,3]

root_node = binary_tree.build_tree(tree_values)

tree_values2 = [5,4,6,None, None, 3,7]
root_node2 = binary_tree.build_tree(tree_values2)





def isValidBST(root) -> bool:

    top_head = root

    def isBST(root, parent_val, side):

        if not root:
            return True
        
        if side == 'left' and root.val < top_head.val:
            return False
        
        if side == 'right' and root.val > top_head.val:
            return False
    
        if side == 'left' and root.val >= parent_val:
            return False
        elif side == 'right' and root.val <= parent_val:
            return False

        left_res = isBST(root.left, root.val, 'left')
        right_res = isBST(root.right, root.val, 'right')

        return left_res and right_res


    if not root:
        return True

    left_res = isBST(root.left, root.val, 'left')
    right_res = isBST(root.right, root.val, 'right')

    return left_res and right_res


# print(isValidBST(root_node))
print(isValidBST(root_node2))