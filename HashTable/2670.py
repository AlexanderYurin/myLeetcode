from typing import List


def distinctDifferenceArray(nums: List[int]) -> List[int]:
	return [len(set(nums[:i + 1])) - len(set(nums[i + 1:])) for i in range(len(nums))]


if __name__ == '__main__':
	assert distinctDifferenceArray(nums=[1, 2, 3, 4, 5]) == [-3, -1, 1, 3, 5]
	assert distinctDifferenceArray(nums=[3, 2, 3, 4, 2]) == [-2, -1, 0, 2, 3]
