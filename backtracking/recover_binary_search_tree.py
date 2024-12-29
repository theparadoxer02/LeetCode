from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree_node(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while i < len(arr):
        current = queue.pop(0)
        
        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

    return root


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        temp = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            temp.append(root)
            inorder(root.right)

        inorder(root)
        N = len(temp)
        ttt = None  
        sec_bug = None
        first_bug = None

        for index in range(N-1):
            if not first_bug and temp[index].val > temp[index +1].val:
                first_bug = temp[index]
                ttt = index + 1
                break

        for index in range(N)[ttt:]:
            if temp[index].val <= temp[ttt].val:
                sec_bug = temp[index]
        
        first_bug.val, sec_bug.val = sec_bug.val, first_bug.val
        return root


arr = [1, 3, None, None, 2]
arr = [12, 10, 15, 5, 13, 6, 16]  # -->  [5, 13, 10 , 12, 6, 15, 16]
root = list_to_tree_node(arr)

S = Solution()
result = S.recoverTree(root=root)
print(result)
