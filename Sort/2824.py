from typing import List


def countPairs(nums: List[int], target: int) -> int:
	result = 0
	nums.sort()
	for num in range(len(nums)):
		result += len([n for n in nums[num + 1:] if target - nums[num] > n])
	return result


if __name__ == '__main__':
	assert countPairs(nums=[-1, 1, 2, 3, 1], target=2) == 3
