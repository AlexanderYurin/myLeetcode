from typing import List


def sumIndicesWithKSetBits(nums: List[int], k: int) -> int:
	result = 0
	for i in range(len(nums)):
		if bin(i).count("1") == k:
			result += nums[i]
	return result


if __name__ == '__main__':
	assert sumIndicesWithKSetBits(nums=[5, 10, 1, 5, 2], k=1) == 13
	assert sumIndicesWithKSetBits(nums=[4, 3, 2, 1], k=2) == 1
