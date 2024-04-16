# Definition for a binary tree node.
import string
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    alphabet = string.ascii_lowercase
    result = ["z"*25]
    def _smallestFromLeaf(root, word=""):
        if not root:
            return
        if root and not root.left and not root.right:
            if result:
                curr_word = (word + alphabet[root.val])[::-1]
                min_word = result.pop()
                if min_word > curr_word:
                    result.append(curr_word)
                else:
                    result.append(min_word)
                return
            result.append(root.val)
        _smallestFromLeaf(root.left, word+alphabet[root.val])
        _smallestFromLeaf(root.right, word+alphabet[root.val])

    _smallestFromLeaf(root)
    return result.pop()


a = TreeNode(2)
a.left = TreeNode(2)
a.right = TreeNode(1)
a.left.right = TreeNode(1)
a.left.right.left = TreeNode(0)
a.right.left = TreeNode(0)
# a.right.right = TreeNode(4)

print(smallestFromLeaf(a))