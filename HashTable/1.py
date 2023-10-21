from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
	num = 0
	count = 1

	while True:
		if count == len(nums):
			num += 1
			count = num + 1
			continue
		if nums[num] + nums[count] == target:
			return [num, count]

		count += 1


if __name__ == '__main__':
	assert twoSum(nums=[11, 15, 2, 7], target=9) == [2, 3]
	assert twoSum(nums=[3, 2, 4], target=6) == [1, 2]
