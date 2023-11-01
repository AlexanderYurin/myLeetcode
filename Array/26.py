from typing import List


def removeDuplicates(nums: List[int]) -> int:
	count = 1
	for i in range(1, len(nums)):
		if nums[i] != nums[i - 1]:
			nums[count] = nums[i]
			count += 1
	return count


if __name__ == '__main__':
	assert removeDuplicates([1, 1, 2]) == 2
	assert removeDuplicates([1]) == 1
	print(nums)
