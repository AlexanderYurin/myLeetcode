from typing import List
from collections import defaultdict


def maxOperations(nums: List[int], k: int) -> int:
    sums_nums = defaultdict(list)
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] <= k:
            if nums[i] in sums_nums:
                count += 1
                if len(sums_nums[nums[i]]) == 1:
                    sums_nums.pop(nums[i])
                else:
                    sums_nums[nums[i]].pop()
            else:
                sums_nums[k - nums[i]].append(nums[i])
        i += 1
    return count


if __name__ == '__main__':
    assert maxOperations(nums=[2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], k=3) == 4
    assert maxOperations(nums=[3, 1, 3, 4, 3], k=6) == 1
