from typing import List


def numberOfPoints(nums: List[List[int]]) -> int:
    result = set()
    for array in nums:
        result.update(list(range(array[0], array[1]+1)))
    return len(set(result))


if __name__ == '__main__':
    assert numberOfPoints(nums = [[3,6],[1,5],[4,7]]) == 7
    assert numberOfPoints(nums = [[1,3],[5,8]]) == 7
