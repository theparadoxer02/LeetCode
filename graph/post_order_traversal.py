def postorderTraversal(root) -> list[int]:

    def post_order(root):
        if not root:
            return []

        pre_nodes = post_order(root.left)
        post_nodes = post_order(root.right)
        root_nodes = [root.val]
        return pre_nodes + post_nodes + root_nodes

    return post_order(root)



postorderTraversal()