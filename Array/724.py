from typing import List


def pivotIndex(nums: List[int]) -> int:
	left_sum = 0
	right_sum = sum(nums)

	for i, elem in enumerate(nums):
		right_sum -= elem
		if left_sum == right_sum:
			return i
		left_sum += elem
	else:
		return -1


if __name__ == '__main__':
	assert pivotIndex(nums=[1, 2, 3]) == -1
