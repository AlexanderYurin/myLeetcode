from typing import List
from itertools import chain


def countNegatives(grid: List[List[int]]) -> int:
    count = 0

    for arr in grid:
        left = 0
        right = len(grid[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < 0:
                right = mid - 1

            else:
                left = mid + 1
        count += len(arr) - left
    return count
    #
    # for i in grid:
    #     l = 0
    #     r = len(grid[0]) - 1
    #     ch = False
    #     while l <= r:
    #         mid = (l + r) >> 1
    #         if i[mid] < 0:
    #             ch = True
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    #     if ch:
    #         c += (len(i) - l)
    # return c
    # arr = list(chain(*grid))
    #
    # return len(list(filter(lambda x: x < 0, chain(grid))))


if __name__ == '__main__':
    assert countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8
