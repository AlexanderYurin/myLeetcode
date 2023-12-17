from typing import List


def increasingTriplet(nums: List[int]) -> bool:
	first = second = float("inf")

	for i in range(len(nums)):
		if nums[i] <= first:
			first = nums[i]
		elif nums[i] <= second:
			second = nums[i]
		else:
			return True
	return False



if __name__ == '__main__':
	assert increasingTriplet(nums=[2, 100, 10, 12]) is True
	assert increasingTriplet(nums=[1, 2, 3, 4, 5]) is True
	assert increasingTriplet(nums=[5, 4, 3, 2, 1]) is False
	assert increasingTriplet(nums=[2, 1, 5, 0, 4, 6]) is True
