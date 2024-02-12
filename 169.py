from collections import Counter
from typing import List


def majorityElement(nums: List[int]) -> int:
    return next(filter(lambda x: x[1] > len(nums) // 2, Counter(nums).items()))[0]

if __name__ == '__main__':
    assert majorityElement(nums=[3, 2, 3]) == 3
