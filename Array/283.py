from typing import List


def moveZeroes(nums: List[int]) -> None:
	"""
    Do not return anything, modify nums in-place instead.
    """

	# nums.sort(key=lambda x: x == 0)
	# return nums
	n = 0
	for i in range(len(nums)):
		if nums[i]:
			nums[n], nums[i] = nums[i], nums[n]
			n += 1


if __name__ == '__main__':
	assert moveZeroes([0, 0, 1]) == [1, 0, 0]
