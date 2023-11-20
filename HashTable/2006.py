from collections import defaultdict
from typing import List


def countKDifference(nums: List[int], k: int) -> int:
	# i < j such that |nums[i] - nums[j]| == k
	# c, i, j = 0, 0, 1
	# while i != len(nums):
	# 	if j < len(nums):
	# 		if abs(nums[i] - nums[j]) == k:
	# 			c += 1
	# 		j += 1
	# 	else:
	# 		i += 1
	# 		j = i + 1
	# return c
	# data = {}
	# count = 0
	# for i in range(len(nums) - 1):
	# 	if nums[i] not in data:
	# 		data[nums[i]] = {k + nums[i]}
	# 		if nums[i] >= k:
	# 			data[nums[i]].add(abs(k - nums[i]))
	# 	count += len([num for num in nums[i + 1:] if num in data[nums[i]]])
	# return count

	seen = defaultdict(int)
	counter = 0
	for num in nums:
		counter += seen[num - k] + seen[num + k]
		seen[num] += 1
	return counter


if __name__ == '__main__':
	assert countKDifference(nums=[1, 2, 2, 1], k=1) == 4
	assert countKDifference(nums=[7, 7, 8, 3, 1, 2, 7, 2, 9, 5], k=6) == 6
	assert countKDifference(nums=[3, 2, 1, 5, 4], k=2) == 3
