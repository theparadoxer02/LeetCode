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
tree_values = [1,2,3,None,5,None,4]
root_node = binary_tree.build_tree(tree_values)

print('abc')
# 'root_node' now represents the root of the binary tree.


def rightSideView(root):
    final_list = []

    def traverse_right(root, depth):
        if not root:
            return final_list
        
        if depth == len(final_list):
            final_list.append(root.val)

        # if root.right:
        traverse_right(root.right, depth + 1)
        traverse_right(root.left, depth + 1)

    traverse_right(root, 0)
    return final_list


final_list = rightSideView(root=root_node)
print(final_list)

    