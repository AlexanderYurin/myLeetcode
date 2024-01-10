from typing import List


def longestSubarray(nums: List[int]) -> int:
	i = k = 0
	count = 0
	max_curr = 0
	for j in range(len(nums)):
		if nums[j] == 0:
			if count == 1:
				i, k = k + 1, j
			else:
				k = j
				count = 1
		max_curr = max(j - i, max_curr)

	return max_curr


if __name__ == '__main__':
	assert longestSubarray(nums=[1, 1, 1]) == 2
	assert longestSubarray(nums=[0, 0, 0, 0]) == 0
	assert longestSubarray(nums=[1, 1, 0, 1]) == 3
	assert longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
