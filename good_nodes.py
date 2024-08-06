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
tree_values = [3,1,4,3,None,1,5]
root_node = binary_tree.build_tree(tree_values)

print('abc')
# 'root_node' now represents the root of the binary tree.


def goodNodes(root) -> int:
    final_list = []

    def rightpath(root, curr_val):
        if not root:
            return
        
        if root.val >= curr_val:
            final_list.append(root.val)

        rightpath(root.left, root.val)
        rightpath(root.right, root.val)

    rightpath(root, 0)
    return len(final_list)


final_list = goodNodes(root=root_node)
print(final_list)

    