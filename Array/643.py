from functools import reduce
from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
	max_cur = max_sum = sum(nums[:k])
	for i in range(k, len(nums)):
		max_cur += nums[i] - nums[i - k]
		if max_cur > max_sum:
			max_sum = max_cur

	return max_sum / k


if __name__ == '__main__':
	assert findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4) == 12.75000
	assert findMaxAverage([0, 4, 0, 3, 2], 1) == 4.0
