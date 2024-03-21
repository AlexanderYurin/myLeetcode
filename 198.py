from collections import deque
from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) > 2:
        res = deque([nums[0], nums[1]])
        if nums[0] > nums[1]:
            res.pop()
            res.append(nums[0])
        for i in range(2, len(nums)):
            x = res[0] + nums[i]
            y = res[1]
            res.append(max(x, y))
            res.popleft()
        return max(res)
    return max(nums)


assert rob(nums = [1,2,3,1]) == 4
assert rob(nums = [2,1,1,2]) == 4




