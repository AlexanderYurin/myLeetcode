from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Алгоритм
        Для начала устанавливаем флаг направления и берем переменную глубины
        в методе _longestZigZag реализуем рекурсивное прохождение по бинарному дереву



        """

        def _longestZigZag(
                root: Optional[TreeNode], isLeft: bool, deep: int
        ):
            if not root:
                return deep
            if isLeft:
                deep = max(
                    deep,
                    _longestZigZag(root.right, False, deep + 1),
                    _longestZigZag(root.left, True, 0),
                )
            else:
                deep = max(
                    deep,
                    _longestZigZag(root.left, True, deep + 1),
                    _longestZigZag(root.right, False, 0),
                )
            return deep

        return max(
            _longestZigZag(root.left, True, 0),
            _longestZigZag(root.right, False, 0),
        )





