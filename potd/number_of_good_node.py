# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/

def countPairs(self, root):
    lead_nodes = []

    def dfs(node):
        if not node:
            return

        print(node.val)

        if not node.left and not node.right:
            lead_nodes.append(node.val)

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    print(lead_nodes)


