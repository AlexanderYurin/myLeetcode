from collections import Counter
from typing import List


def maxFrequencyElements(nums: List[int]) -> int:
	hash_nums = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
	maximum_frequency = hash_nums[0][1]
	result = 0
	for arr in hash_nums:
		if arr[1] == maximum_frequency:
			result += arr[1]
	return result


if __name__ == '__main__':
	assert maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4]) == 4
