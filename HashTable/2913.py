from typing import List
from collections import Counter


def sumCounts(nums: List[int]) -> int:
    result = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            result += len(set(nums[i:j + 1]))**2
    return result


if __name__ == '__main__':
    assert sumCounts(nums=[1, 2, 1]) == 15
    assert sumCounts(nums=[1, 1]) == 3
