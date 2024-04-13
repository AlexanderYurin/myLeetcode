from collections import deque
from typing import List


def minPairSum(nums: List[int]) -> int:
    nums.sort()
    nums = deque(nums)
    min_max_sum_pair = 0
    while nums:
        curr_sum_pair = nums.popleft() + nums.pop()
        if min_max_sum_pair < curr_sum_pair:
            min_max_sum_pair = curr_sum_pair
    return min_max_sum_pair
