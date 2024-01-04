# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    total_nums = len(nums)
    if not total_nums:
        return None

    mid_node = total_nums // 2
    return TreeNode(
        nums[mid_node],
        sortedArrayToBST(nums[:mid_node]), sortedArrayToBST(nums[mid_node + 1:]))


sortedArrayToBST([-10, -3, 0, 5, 9])
