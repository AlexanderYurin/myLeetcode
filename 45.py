from typing import List


def jump(nums: List[int]) -> int:
	i = 0
	len_nums = len(nums) - 1
	count = 0
	while i < len_nums:
		count += 1
		if nums[i] + i >= len_nums:
			break
		j = 0
		max_jump = 0
		for k in range(1, nums[i] + 1):
			if max_jump <= nums[i + k] + k:
				max_jump = nums[i + k] + k
				j = k
		else:
			i += j
	return count


assert jump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]) == 3
assert jump([2, 3, 1]) == 1
assert jump([2, 1]) == 1
assert jump([1, 1, 2, 1, 1]) == 3
assert jump([4, 1, 1, 3, 1, 1, 1]) == 2
assert jump([1, 1, 2, 1, 1]) == 3
assert jump([2, 3, 1, 1, 4]) == 2
assert jump([1, 2, 3, 4]) == 2
assert jump([2, 3, 0, 1, 4]) == 2
