from typing import List


def minimumRightShifts(nums: List[int]) -> int:

	# sort_nums = repr(sorted(nums))
	# count = 0
	# while repr(nums) != sort_nums:
	# 	if nums[-1] > nums[0]:
	# 		return -1
	# 	count += 1
	# 	num = nums.pop()
	# 	nums.insert(0, num)
	# return count
	n = len(nums)

	for i in range(1, n):
		if nums[i] < nums[i - 1]:
			nums = nums[i:] + nums[:i]
			return n - i if nums == sorted(nums) else -1

	return 0


if __name__ == '__main__':
	assert minimumRightShifts(nums=[3, 4, 5, 1, 2]) == 2
	assert minimumRightShifts(nums=[3, 4, 5, 1, 2]) == 2
