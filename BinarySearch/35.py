from typing import List


def searchInsert(nums: List[int], target: int) -> int:
	low = 0
	high = len(nums) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = nums[mid]
		if guess == target:
			return mid
		if guess > target:
			high = mid - 1
		else:
			low = mid + 1
	else:
		return low


assert searchInsert([1, 3, 5, 6], 0) == 0
assert 2 == searchInsert([1, 3, 5, 6], 4)
assert searchInsert([1, 3, 5, 6], 7) == 4
